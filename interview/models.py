from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    target_role = models.CharField(max_length=100, blank=True, null=True, default="Software Engineer")
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()

class InterviewSession(models.Model):
    INTERVIEW_TYPES = [
        ('hr', 'HR Interview (Non-Technical)'),
        ('behavioral', 'Behavioral Interview (Non-Technical)'),
        ('leadership', 'Leadership & Communication (Non-Technical)'),
        ('python', 'Python & Software Engineering (Technical)'),
        ('webdev', 'Web Development (Technical)'),
        ('db_sql', 'Databases & SQL (Technical)'),
        ('dsa', 'Data Structures & Algorithms (Technical)'),
        ('aptitude', 'Aptitude & Logical Reasoning (Technical)'),
        ('programming', 'Programming & Coding (Technical)'),
        ('adaptive', 'Adaptive HR & Stress Round'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sessions')
    interview_type = models.CharField(max_length=50, choices=INTERVIEW_TYPES)
    job_role = models.CharField(max_length=100, default='Software Developer')
    used_questions_json = models.JSONField(default=list, blank=True)
    used_interruptions_json = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    final_score = models.IntegerField(blank=True, null=True)
    feedback_summary = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='in_progress') # in_progress, completed
    
    # Stress & Cognitive extensions
    pressure_level = models.CharField(max_length=20, default='none') # 'none', 'low', 'medium', 'high'
    is_cognitive = models.BooleanField(default=False)
    score_stress_handling = models.IntegerField(default=0)
    score_cognitive_reasoning = models.IntegerField(default=0)
    score_problem_solving = models.IntegerField(default=0)
    score_technical_explanation = models.IntegerField(default=0)
    score_technical_communication = models.IntegerField(default=0)
    
    # Advanced Heuristics metadata
    consistency_check = models.CharField(max_length=50, default='Strong')
    consistency_feedback = models.TextField(blank=True, null=True)
    self_awareness_indicator = models.CharField(max_length=50, default='High')
    self_awareness_feedback = models.TextField(blank=True, null=True)
    adaptation_details = models.TextField(blank=True, null=True)

    # Audio quality & answer status tracking
    total_no_answers = models.IntegerField(default=0)
    total_skipped = models.IntegerField(default=0)
    total_noise_events = models.IntegerField(default=0)
    total_relevant = models.IntegerField(default=0)
    total_partially_relevant = models.IntegerField(default=0)
    total_not_relevant = models.IntegerField(default=0)
    total_short_answers = models.IntegerField(default=0)
    audio_quality_summary = models.CharField(max_length=50, default='Good')

    def __str__(self):
        return f"{self.user.username} - {self.get_interview_type_display()} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class ResponseEvaluation(models.Model):
    session = models.ForeignKey(InterviewSession, on_delete=models.CASCADE, related_name='evaluations')
    question_text = models.TextField()
    transcript_text = models.TextField(blank=True, null=True)
    programming_language = models.CharField(max_length=20, blank=True, null=True)
    audio_file = models.FileField(upload_to='interview_audio/', blank=True, null=True)
    video_file = models.FileField(upload_to='interview_video/', blank=True, null=True)
    eye_contact_score = models.IntegerField(default=0) # score out of 20
    posture_score = models.IntegerField(default=0) # score out of 20
    video_feedback = models.TextField(blank=True, null=True)
    duration_seconds = models.FloatField(default=0.0)
    words_count = models.IntegerField(default=0)
    words_per_minute = models.FloatField(default=0.0)
    
    # Store filler word counts, grammar errors, and keywords as JSON
    filler_words_json = models.JSONField(default=dict, blank=True)
    sentiment = models.CharField(max_length=20, blank=True, null=True) # Positive, Neutral, Negative
    confidence_score = models.FloatField(default=0.0) # Score out of 100
    grammar_errors_json = models.JSONField(default=list, blank=True)
    keywords_found_json = models.JSONField(default=list, blank=True)
    
    # Parameter breakdown scores (out of 20 each)
    score_confidence = models.IntegerField(default=0)
    score_grammar = models.IntegerField(default=0)
    score_communication = models.IntegerField(default=0)
    score_sentiment = models.IntegerField(default=0)
    score_filler_words = models.IntegerField(default=0)

    # Answer & Noise Detection fields
    answer_status = models.CharField(max_length=20, default='answered') # answered, no_answer, skipped, too_short, not_relevant, partially_relevant
    relevance_category = models.CharField(max_length=30, default='relevant') # no_answer, short_answer, not_relevant, partially_relevant, relevant, strong
    relevance_feedback = models.TextField(blank=True, null=True)
    audio_quality = models.CharField(max_length=20, default='good') # good, high_noise, audio_unclear, unreliable
    noise_events_count = models.IntegerField(default=0)
    audio_quality_feedback = models.TextField(blank=True, null=True)
    
    overall_score = models.IntegerField(default=0) # out of 100
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Response for Session {self.session.id} - Q: {self.question_text[:30]}..."

class InterviewRecording(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_recordings')
    video = models.FileField(upload_to='interview_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=20, default="01:24")
    status = models.CharField(max_length=20, default="completed")
    overall_score = models.IntegerField(default=88)

    def __str__(self):
        return f"{self.user.username} - Video Recording #{self.id}"

class StressAnalysis(models.Model):
    evaluation = models.OneToOneField(ResponseEvaluation, on_delete=models.CASCADE, related_name='stress_analysis')
    is_interrupted = models.BooleanField(default=False)
    interruption_prompt = models.TextField(blank=True, null=True)
    reaction_time = models.FloatField(default=0.0)      # seconds taken to speak after interruption
    recovery_time = models.FloatField(default=0.0)      # seconds taken to stabilize speaking speed
    filler_words_after = models.IntegerField(default=0)  # count of fillers spoken after interruption
    speech_speed_change = models.FloatField(default=0.0) # WPM variance before vs after
    stability_score = models.IntegerField(default=0)     # out of 100
    stress_score = models.IntegerField(default=0)        # out of 100 (Stress Handling Score)

    def __str__(self):
        return f"Stress Analysis for evaluation {self.evaluation.id}"

class CognitiveAnalysis(models.Model):
    evaluation = models.OneToOneField(ResponseEvaluation, on_delete=models.CASCADE, related_name='cognitive_analysis')
    time_taken = models.FloatField(default=0.0)
    attempts_count = models.IntegerField(default=1)
    logical_steps_json = models.JSONField(default=list, blank=True)
    explanation_quality = models.IntegerField(default=0)
    code_correctness = models.IntegerField(default=0)
    complexity_explanation_score = models.IntegerField(default=0)
    cognitive_score = models.IntegerField(default=0)
    problem_solving_score = models.IntegerField(default=0)
    explanation_score = models.IntegerField(default=0)
    tech_comm_score = models.IntegerField(default=0)
    
    # Real-time reasoning flow stages statuses
    understand_stage = models.BooleanField(default=True)
    plan_stage = models.BooleanField(default=True)
    solve_stage = models.BooleanField(default=True)
    explain_stage = models.BooleanField(default=True)
    verify_stage = models.BooleanField(default=True)

    def __str__(self):
        return f"Cognitive Analysis for evaluation {self.evaluation.id}"


# ----------------- Learning Center Platform Models -----------------

class LearningCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    icon = models.CharField(max_length=50, default='fa-book')
    description = models.TextField(blank=True, null=True)
    category_type = models.CharField(max_length=50, default='general') # hr, technical, communication, coding, project, resume, stress
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = 'Learning Categories'

    def __str__(self):
        return self.name

class LearningTopic(models.Model):
    category = models.ForeignKey(LearningCategory, on_delete=models.CASCADE, related_name='topics')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    difficulty = models.CharField(max_length=20, default='Beginner') # Beginner, Intermediate, Advanced
    order = models.IntegerField(default=0)
    summary = models.TextField(blank=True, null=True)
    explanation = models.TextField()
    real_world_example = models.TextField(blank=True, null=True)
    interview_question = models.TextField(blank=True, null=True)
    sample_answer = models.TextField(blank=True, null=True)
    common_mistake = models.TextField(blank=True, null=True)
    practical_tip = models.TextField(blank=True, null=True)
    practice_question = models.TextField(blank=True, null=True)
    practice_options_json = models.JSONField(default=list, blank=True)
    correct_option_index = models.IntegerField(default=0, blank=True, null=True)
    
    # Coding problem extensions
    is_coding = models.BooleanField(default=False)
    code_initial = models.TextField(blank=True, null=True)
    code_hint = models.TextField(blank=True, null=True)
    code_solution = models.TextField(blank=True, null=True)
    example_input = models.CharField(max_length=200, blank=True, null=True)
    example_output = models.CharField(max_length=200, blank=True, null=True)
    time_complexity = models.CharField(max_length=100, blank=True, null=True)
    space_complexity = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.category.name} - {self.title}"

class UserLearningProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='learning_progress')
    topic = models.ForeignKey(LearningTopic, on_delete=models.CASCADE, related_name='user_progress')
    is_completed = models.BooleanField(default=False)
    is_bookmarked = models.BooleanField(default=False)
    quiz_attempted = models.BooleanField(default=False)
    quiz_correct = models.BooleanField(default=False)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'topic')

    def __str__(self):
        return f"{self.user.username} - {self.topic.title} (Completed: {self.is_completed})"

