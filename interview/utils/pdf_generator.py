from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from interview.utils.nlp_analyzer import QUESTION_KEYWORDS


def generate_interview_pdf(session):
    """
    Generates a PDF report for an InterviewSession using ReportLab.
    Returns a bytes buffer containing the PDF file.
    """
    buffer = BytesIO()
    
    # Page setup
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=54, # 0.75 in
        leftMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom Palette
    PRIMARY_COLOR = colors.HexColor("#1e293b")   # Slate 800
    SECONDARY_COLOR = colors.HexColor("#4f46e5") # Indigo 600
    TEXT_COLOR = colors.HexColor("#334155")      # Slate 700
    BG_LIGHT = colors.HexColor("#f8fafc")        # Slate 50
    ACCENT_GREEN = colors.HexColor("#10b981")    # Emerald 500
    LINE_COLOR = colors.HexColor("#e2e8f0")      # Slate 200
    
    # Text styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=26,
        leading=32,
        textColor=PRIMARY_COLOR,
        spaceAfter=10
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#64748b"),
        spaceAfter=25
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=PRIMARY_COLOR,
        spaceBefore=15,
        spaceAfter=10,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=TEXT_COLOR
    )
    
    bold_body_style = ParagraphStyle(
        'BoldBodyTextCustom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=14,
        textColor=PRIMARY_COLOR
    )
    
    score_label_style = ParagraphStyle(
        'ScoreLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=colors.white,
        alignment=1 # Centered
    )
    
    score_num_style = ParagraphStyle(
        'ScoreNum',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=36,
        leading=42,
        textColor=colors.white,
        alignment=1 # Centered
    )

    # 1. Document Header
    story.append(Paragraph("Interview Performance Report", title_style))
    story.append(Paragraph(f"Candidate: {session.user.first_name} {session.user.last_name} ({session.user.username})  |  Date: {session.created_at.strftime('%B %d, %Y')}", subtitle_style))
    story.append(Spacer(1, 10))
    
    # 2. Hero Section (Info Table & Score Box side by side)
    # Left column: Candidate & Session Metadata
    meta_data = [
        [Paragraph("Interview Type:", bold_body_style), Paragraph(session.get_interview_type_display(), body_style)],
        [Paragraph("Target Role:", bold_body_style), Paragraph(session.user.profile.target_role or "N/A", body_style)],
        [Paragraph("Total Questions:", bold_body_style), Paragraph(str(session.evaluations.count()), body_style)],
        [Paragraph("Status:", bold_body_style), Paragraph(session.status.upper(), body_style)],
    ]
    meta_table = Table(meta_data, colWidths=[1.5*inch, 2.5*inch])
    meta_table.setStyle(TableStyle([
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
    ]))
    
    # Right column: Overall Score Box
    score_data = [
        [Paragraph("OVERALL SCORE", score_label_style)],
        [Paragraph(f"{session.final_score or 0}", score_num_style)],
        [Paragraph("out of 100", score_label_style)]
    ]
    score_table = Table(score_data, colWidths=[2.0*inch])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), SECONDARY_COLOR),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
    ]))
    
    # Master Hero Table
    hero_table = Table([[meta_table, score_table]], colWidths=[4.2*inch, 2.8*inch])
    hero_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 1, LINE_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 15),
        ('BOTTOMPADDING', (0,0), (-1,-1), 15),
        ('LEFTPADDING', (0,0), (-1,-1), 15),
        ('RIGHTPADDING', (0,0), (-1,-1), 15),
    ]))
    
    story.append(hero_table)
    story.append(Spacer(1, 20))
    
    # 3. Parameter Breakdown Table
    story.append(Paragraph("Evaluation Parameter Breakdown", h1_style))
    
    # Aggregate parameters across responses
    evals = session.evaluations.all()
    count = evals.count()
    
    avg_conf = sum(e.score_confidence for e in evals) / count * 5 if count > 0 else 0 # back to 100 scale
    avg_grammar = sum(e.score_grammar for e in evals) / count * 5 if count > 0 else 0
    avg_comm = sum(e.score_communication for e in evals) / count * 5 if count > 0 else 0
    avg_sentiment = sum(e.score_sentiment for e in evals) / count * 5 if count > 0 else 0
    avg_filler = sum(e.score_filler_words for e in evals) / count * 5 if count > 0 else 0
    
    def get_status_label(val):
        if val >= 85: return "Excellent"
        elif val >= 70: return "Good"
        elif val >= 50: return "Needs Improvement"
        return "Critical Attention"

    breakdown_data = [
        [Paragraph("Parameter", bold_body_style), Paragraph("Average Score", bold_body_style), Paragraph("Performance Level", bold_body_style)],
        [Paragraph("Confidence & Vocabulary", body_style), Paragraph(f"{round(avg_conf, 1)}%", body_style), Paragraph(get_status_label(avg_conf), body_style)],
        [Paragraph("Grammar & Accuracy", body_style), Paragraph(f"{round(avg_grammar, 1)}%", body_style), Paragraph(get_status_label(avg_grammar), body_style)],
        [Paragraph("Communication & Speaking Pace", body_style), Paragraph(f"{round(avg_comm, 1)}%", body_style), Paragraph(get_status_label(avg_comm), body_style)],
        [Paragraph("Tone & Sentiment", body_style), Paragraph(f"{round(avg_sentiment, 1)}%", body_style), Paragraph(get_status_label(avg_sentiment), body_style)],
        [Paragraph("Filler Words Control", body_style), Paragraph(f"{round(avg_filler, 1)}%", body_style), Paragraph(get_status_label(avg_filler), body_style)],
    ]
    
    breakdown_table = Table(breakdown_data, colWidths=[3.0*inch, 1.8*inch, 2.2*inch])
    breakdown_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BG_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.5, LINE_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(breakdown_table)
    story.append(Spacer(1, 20))
    
    # 4. Overall Feedback Summary
    story.append(Paragraph("Overall Feedback & Suggestions", h1_style))
    feedback_text = session.feedback_summary or "No summary feedback generated."
    story.append(Paragraph(feedback_text.replace("\n", "<br/>"), body_style))
    story.append(Spacer(1, 25))
    
    # Page Break for Question Details
    story.append(PageBreak())
    
    # 5. Question by Question Details
    story.append(Paragraph("Detailed Question Responses", title_style))
    story.append(Spacer(1, 10))
    
    question_num = 1
    for evaluation in evals:
        # Question Header
        q_label = f"Question {question_num}"
        if evaluation.programming_language:
            q_label += f" ({evaluation.programming_language})"
        story.append(Paragraph(f"{q_label}: {evaluation.question_text}", h1_style))
        
        # Transcript Box
        transcript_label = Paragraph("Candidate Answer Transcript:", bold_body_style)
        transcript_p = Paragraph(evaluation.transcript_text or "[Silent response]", body_style)
        
        # Analysis Row
        wpm_txt = f"{evaluation.words_per_minute} WPM ({evaluation.words_count} words)"
        sentiment_txt = f"{evaluation.sentiment}"
        
        fillers = []
        for word, cnt in evaluation.filler_words_json.items():
            fillers.append(f"{word}: {cnt}")
        fillers_txt = ", ".join(fillers) if fillers else "None detected"
        
        metrics_data = [
            [Paragraph("Speech Speed:", bold_body_style), Paragraph(wpm_txt, body_style), 
             Paragraph("Filler Words:", bold_body_style), Paragraph(fillers_txt, body_style)],
            [Paragraph("Sentiment:", bold_body_style), Paragraph(sentiment_txt, body_style), 
             Paragraph("Score:", bold_body_style), Paragraph(f"{evaluation.overall_score}/100", bold_body_style)]
        ]
        if evaluation.video_file or evaluation.eye_contact_score > 0:
            metrics_data.append([
                Paragraph("Eye Contact:", bold_body_style), Paragraph(f"{evaluation.eye_contact_score}/20", body_style),
                Paragraph("Posture Score:", bold_body_style), Paragraph(f"{evaluation.posture_score}/20", body_style)
            ])
        metrics_table = Table(metrics_data, colWidths=[1.2*inch, 2.3*inch, 1.2*inch, 2.3*inch])
        metrics_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('GRID', (0,0), (-1,-1), 0.5, LINE_COLOR),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
            ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT)
        ]))
        
        # Grammar & Keywords details
        grammar_errs = evaluation.grammar_errors_json
        grammar_txt = ""
        if grammar_errs:
            grammar_list = []
            for err in grammar_errs:
                grammar_list.append(f"• <b>{err.get('type', 'Error')}</b>: {err.get('message', '')} <i>Correction: {err.get('suggestion', '')}</i>")
            grammar_txt = "<br/>".join(grammar_list)
        else:
            grammar_txt = "No grammar errors detected!"
            
        kws_found = evaluation.keywords_found_json
        expected = QUESTION_KEYWORDS.get(evaluation.question_text, [])
        kws_missing = [k for k in expected if k not in kws_found]
        
        keyword_parts = []
        if kws_found:
            keyword_parts.append(f"<b>Keywords Found:</b> {', '.join(kws_found)}")
        if kws_missing:
            keyword_parts.append(f"<b>Suggested Keywords to Add:</b> {', '.join(kws_missing)}")
        keyword_txt = "<br/>".join(keyword_parts) if keyword_parts else "No specific keywords matching required."
        
        # Feedback block
        feedback_label = Paragraph("Evaluator Feedback & Suggestions:", bold_body_style)
        feedback_p = Paragraph(evaluation.feedback or "No feedback recorded.", body_style)
        
        # Add everything to story
        story.append(transcript_label)
        story.append(Spacer(1, 4))
        story.append(transcript_p)
        story.append(Spacer(1, 10))
        story.append(metrics_table)
        story.append(Spacer(1, 10))
        
        story.append(Paragraph("Grammar Analysis:", bold_body_style))
        story.append(Spacer(1, 4))
        story.append(Paragraph(grammar_txt, body_style))
        story.append(Spacer(1, 10))
        
        story.append(Paragraph("Keyword Matching:", bold_body_style))
        story.append(Spacer(1, 4))
        story.append(Paragraph(keyword_txt, body_style))
        story.append(Spacer(1, 10))
        
        story.append(feedback_label)
        story.append(Spacer(1, 4))
        story.append(feedback_p)
        story.append(Spacer(1, 10))
        
        if evaluation.video_file or evaluation.eye_contact_score > 0:
            story.append(Paragraph("AI Video & Presentation Feedback:", bold_body_style))
            story.append(Spacer(1, 4))
            story.append(Paragraph(evaluation.video_feedback or "No visual suggestions.", body_style))
            story.append(Spacer(1, 10))
        
        story.append(Spacer(1, 15))
        story.append(Table([[colors.HexColor("#cbd5e1")]], colWidths=[7.0*inch], rowHeights=[1])) # Divider
        story.append(Spacer(1, 15))
        
        question_num += 1
        
    doc.build(story)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
