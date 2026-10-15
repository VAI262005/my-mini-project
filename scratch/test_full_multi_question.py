import os
import sys
import django

sys.path.insert(0, r'C:\Users\ADMIN\.gemini\antigravity\scratch\ai_interview_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_interview_system.settings')
django.setup()

from django.contrib.auth.models import User
from interview.models import InterviewSession, ResponseEvaluation
from django.test import RequestFactory
from interview.views import process_answer_api, INTERVIEW_QUESTIONS

def run_multi_question_test(track):
    print(f"\n==========================================")
    print(f"TESTING FULL MULTI-QUESTION FLOW FOR TRACK: '{track}'")
    print(f"==========================================")
    
    user = User.objects.filter(username='test_candidate').first()
    if not user:
        user = User.objects.create_user('test_candidate', 'test@example.com', 'password123')
        
    session = InterviewSession.objects.create(
        user=user,
        interview_type=track,
        status='in_progress'
    )
    
    factory = RequestFactory()
    questions_bank = INTERVIEW_QUESTIONS.get(track, INTERVIEW_QUESTIONS['hr'])
    current_q_text = questions_bank[0]
    
    q_num = 1
    total_questions = len(questions_bank)
    
    while True:
        print(f"\n--- Submitting Answer for Question {q_num} (Total: {total_questions}) ---")
        print(f"Prompt: '{current_q_text}'")
        
        post_data = {
            'session_id': session.id,
            'question_text': current_q_text,
            'transcript': f"Detailed candidate response for question {q_num} covering key technical and architectural decisions.",
            'duration': '15.0',
            'answer_status': 'answered',
            'audio_quality': 'good',
            'noise_events_count': '0',
            'force_submit': 'true'
        }
        
        request = factory.post('/interview/api/process_answer/', data=post_data)
        request.user = user
        request.session = {}
        
        response = process_answer_api(request)
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}"
        
        import json
        res_json = json.loads(response.content.decode('utf-8'))
        print("API Response:", res_json)
        
        assert res_json.get('success') is True, "Expected 'success': True in JSON response"
        
        if res_json.get('status') == 'completed' or res_json.get('interview_complete'):
            assert 'redirect_url' in res_json, "Missing redirect_url in completion response!"
            print(f"[SUCCESS] Session Completed Successfully! Final redirect: {res_json['redirect_url']}")
            break
        else:
            assert res_json.get('status') == 'next', f"Expected status 'next', got {res_json.get('status')}"
            assert 'next_question' in res_json and res_json['next_question'], "Missing next_question in response!"
            current_q_text = res_json['next_question']
            total_questions = res_json.get('total_questions', total_questions)
            print(f"[SUCCESS] Advanced to Question {res_json['question_number']} of {total_questions}: '{current_q_text}'")
            q_num = res_json['question_number']

if __name__ == '__main__':
    for track in ['hr', 'python', 'webdev', 'dsa', 'adaptive']:
        run_multi_question_test(track)
    print("\nALL MULTI-QUESTION TRACK TESTS PASSED PERFECTLY!")
