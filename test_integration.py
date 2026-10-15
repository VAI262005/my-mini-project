import os
import sys
import django

# Setup Django Environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_interview_system.settings')
django.setup()

from django.contrib.auth.models import User
from interview.models import InterviewSession, ResponseEvaluation
from interview.utils.nlp_analyzer import run_response_evaluation
from interview.utils.pdf_generator import generate_interview_pdf
from interview.views import finalize_interview_session

def run_integration_test():
    print("=== Starting AI Mock Interview & Simplification Integration Test ===")
    
    # 1. Create Directories if they don't exist
    os.makedirs(os.path.join(os.path.dirname(__file__), 'static'), exist_ok=True)
    os.makedirs(os.path.join(os.path.dirname(__file__), 'media'), exist_ok=True)
    print("[OK] Static and media directories validated.")

    # 2. Get or Create Test User
    user, created = User.objects.get_or_create(username='test_candidate', email='test@candidate.com')
    if created:
        user.set_password('candidate123')
        user.first_name = "Vaishnavi"
        user.last_name = "Patil"
        user.save()
        print(f"[OK] Created test candidate: {user.username}")
    else:
        print(f"[OK] Found existing candidate: {user.username}")

    # 3. Create Aptitude Interview Session
    session = InterviewSession.objects.create(
        user=user,
        interview_type='aptitude',
        status='in_progress'
    )
    print(f"[OK] Started Aptitude Session #{session.id}")

    # 4. Question 1: Simplify question with ALL keywords correct
    q1 = "Simplify the expression: 12.5% of 120 plus 37.5% of 240."
    ans1 = "To multiply this, 12.5 percent of 120 is 15, and 37.5 percent of 240 is 90. We add these. Each fraction is computed and the sum is 105."
    dur1 = 20.0
    
    print(f"\nEvaluating Question 1 (Correct Simplification): '{q1}'")
    res1 = run_response_evaluation(q1, ans1, dur1, has_video=False)
    print(f"  Overall Score: {res1['overall_score']}/100 (Expected: 100)")
    print(f"  Feedback: {res1['feedback']}")
    
    assert res1['overall_score'] == 100, "Error: Correct math answer should receive 100 marks!"
    print("[OK] Assertion passed: Correct answer received 100/100 full marks.")
    
    ResponseEvaluation.objects.create(
        session=session, 
        question_text=q1,
        **res1
    )

    # 5. Question 2: Incorrect response (missing keywords/answer is wrong)
    ans2 = "The sum is 95."
    dur2 = 10.0
    
    print(f"\nEvaluating Question 2 (Incorrect Simplification): '{q1}'")
    res2 = run_response_evaluation(q1, ans2, dur2, has_video=False)
    print(f"  Overall Score: {res2['overall_score']}/100 (Expected: 0)")
    print(f"  Feedback: {res2['feedback']}")
    
    assert res2['overall_score'] == 0, "Error: Wrong answer should receive exactly 0 marks!"
    print("[OK] Assertion passed: Wrong math answer successfully scored 0 marks.")
    
    ResponseEvaluation.objects.create(
        session=session, 
        question_text=q1,
        **res2
    )

    # 6. Finalize the Session
    print("\nFinalizing session...")
    finalize_interview_session(session)
    session.refresh_from_db()
    print(f"[OK] Finalized session. Final Score: {session.final_score}/100")

    # 7. Generate and Export PDF
    print("\nGenerating PDF Report...")
    pdf_bytes = generate_interview_pdf(session)
    pdf_path = os.path.join(os.path.dirname(__file__), 'test_interview_report.pdf')
    with open(pdf_path, 'wb') as f:
        f.write(pdf_bytes)
    print(f"[OK] Exported PDF performance report to: {pdf_path}")
    print("=== Integration Test Completed Successfully! ===")

if __name__ == '__main__':
    run_integration_test()
