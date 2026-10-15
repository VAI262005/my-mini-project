import os
import sys
import django

# Set up Django environment
sys.path.insert(0, r'C:\Users\ADMIN\.gemini\antigravity\scratch\ai_interview_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_interview_system.settings')
django.setup()

from django.contrib.auth.models import User
from interview.models import InterviewSession, ResponseEvaluation
from django.test import RequestFactory
from interview.views import process_answer_api, INTERVIEW_QUESTIONS

def test_flow():
    user = User.objects.filter(username='test_candidate').first()
    if not user:
        user = User.objects.create_user('test_candidate', 'test@example.com', 'password123')
    
    # Create an active session
    session = InterviewSession.objects.create(
        user=user,
        interview_type='hr',
        status='in_progress'
    )
    print(f"Created Session ID: {session.id}, Track: hr")
    
    factory = RequestFactory()
    
    # 1. Submit Answer 1
    post_data_1 = {
        'session_id': session.id,
        'question_text': INTERVIEW_QUESTIONS['hr'][0],
        'transcript': 'I am a software engineer with 2 years of experience in Django and Python development.',
        'duration': '15.5',
        'answer_status': 'answered',
        'audio_quality': 'good',
        'noise_events_count': '0',
    }
    
    request = factory.post('/interview/api/process_answer/', data=post_data_1)
    request.user = user
    # Add session middleware mock
    request.session = {}
    
    try:
        response = process_answer_api(request)
        print("Response status code:", response.status_code)
        print("Response content:", response.content.decode('utf-8'))
    except Exception as e:
        print("EXCEPTION OCCURRED IN process_answer_api:")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    test_flow()
