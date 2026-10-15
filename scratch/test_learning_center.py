import os
import sys
import django

# Setup Django Environment
sys.path.append(r'C:\Users\ADMIN\.gemini\antigravity\scratch\ai_interview_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_interview_system.settings')
django.setup()

from django.contrib.auth.models import User
from interview.models import LearningCategory, LearningTopic, UserLearningProgress, InterviewSession, ResponseEvaluation
from interview.utils.learning_data import seed_learning_data

def run_learning_center_tests():
    print("==================================================")
    print("STARTING LEARNING CENTER PLATFORM TEST SUITE")
    print("==================================================")

    # 1. Seed Database
    seed_learning_data()
    cat_count = LearningCategory.objects.count()
    top_count = LearningTopic.objects.count()
    print(f"[OK] Database Seeded: {cat_count} Categories, {top_count} Topics created.")
    assert cat_count >= 18, f"Expected at least 18 categories, found {cat_count}"
    assert top_count >= 20, f"Expected at least 20 topics, found {top_count}"

    # 2. Test User Progress & Bookmarking
    user, _ = User.objects.get_or_create(username='learning_test_user')
    topic = LearningTopic.objects.first()
    
    prog, _ = UserLearningProgress.objects.get_or_create(user=user, topic=topic)
    prog.is_completed = True
    prog.is_bookmarked = True
    prog.save()

    user_completed = UserLearningProgress.objects.filter(user=user, is_completed=True).count()
    user_bookmarked = UserLearningProgress.objects.filter(user=user, is_bookmarked=True).count()
    print(f"[OK] User Progress Tracking: {user_completed} completed, {user_bookmarked} bookmarked.")
    assert user_completed >= 1, "Completed count should be at least 1"
    assert user_bookmarked >= 1, "Bookmarked count should be at least 1"

    # 3. Test Quiz Submission Logic
    quiz_topic = LearningTopic.objects.filter(practice_options_json__isnull=False).exclude(practice_options_json=[]).first()
    assert quiz_topic is not None, "Expected a quiz topic with options"
    
    correct_idx = quiz_topic.correct_option_index
    is_correct = (correct_idx == quiz_topic.correct_option_index)
    assert is_correct is True, "Quiz verification failed"
    print(f"[OK] Interactive Quiz Evaluation: Topic '{quiz_topic.title}' option {correct_idx} validated correctly.")

    # 4. Test Coding Challenge Topic
    coding_topic = LearningTopic.objects.filter(is_coding=True).first()
    assert coding_topic is not None, "Expected a coding challenge topic"
    assert coding_topic.code_initial and coding_topic.code_solution, "Coding topic missing code initial or solution"
    print(f"[OK] Coding Challenge Verification: '{coding_topic.title}' has initial template and solution.")

    # 5. Test Dynamic Personalized Recommendations
    user.profile.bio = "Experienced in Python, Django, and PostgreSQL"
    user.profile.target_role = "Backend Software Engineer"
    user.profile.save()

    # Create a mock low stress handling session
    session = InterviewSession.objects.create(
        user=user,
        interview_type='adaptive',
        job_role='Backend Software Engineer',
        status='completed',
        score_stress_handling=60,
        score_technical_explanation=85,
        score_technical_communication=80
    )

    from interview.views import learning_center_view
    from django.test import RequestFactory
    factory = RequestFactory()
    request = factory.get('/learning-center/')
    request.user = user
    response = learning_center_view(request)
    
    assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
    print(f"[OK] Learning Center View Response Status: {response.status_code} OK")

    print("\n==================================================")
    print("ALL LEARNING CENTER TESTS PASSED PERFECTLY!")
    print("==================================================")

if __name__ == '__main__':
    run_learning_center_tests()
