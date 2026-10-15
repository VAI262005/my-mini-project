import os
import sys
import django
import json

# Setup Django Environment
sys.path.append(r'C:\Users\ADMIN\.gemini\antigravity\scratch\ai_interview_system')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_interview_system.settings')
django.setup()

from django.contrib.auth.models import User
from interview.models import InterviewSession, ResponseEvaluation, StressAnalysis
from interview.utils.question_pool import (
    JOB_ROLE_QUESTION_POOLS,
    select_next_question_for_session,
    get_next_interruption,
    check_semantic_similarity
)

def run_test_suite():
    print("==================================================")
    print("STARTING JOB-ROLE & INTERRUPTION FLOW TEST SUITE")
    print("==================================================")

    user, created = User.objects.get_or_create(username='test_role_user')
    if created:
        user.set_password('password123')
        user.save()

    # --------------------------------------------------
    # TEST 1: Software Developer Interview 1 Flow
    # --------------------------------------------------
    print("\n--- TEST 1: Software Developer Interview #1 Flow ---")
    session1 = InterviewSession.objects.create(
        user=user,
        interview_type='adaptive',
        job_role='Software Developer',
        pressure_level='medium',
        used_questions_json=[],
        used_interruptions_json=[]
    )
    
    # Q1 Setup
    q1 = select_next_question_for_session(session1)
    int1 = get_next_interruption(session1)
    print(f"Q1: {q1}")
    print(f"Interruption 1 ({int1['type']}): {int1['prompt']}")

    # Candidate answers Q1 mentioning Python and Django
    ans1_text = "I have 3 years of experience in Software Development using Python and Django for web backends."
    ev1 = ResponseEvaluation.objects.create(
        session=session1,
        question_text=q1,
        transcript_text=ans1_text,
        duration_seconds=15.0,
        words_count=16,
        overall_score=85
    )
    StressAnalysis.objects.create(
        evaluation=ev1,
        is_interrupted=True,
        interruption_prompt=int1['prompt'],
        reaction_time=1.8,
        recovery_time=4.2,
        stress_score=88
    )

    # Q2 Adaptive Selection based on candidate mentioning Django
    q2 = select_next_question_for_session(session1, last_transcript=ans1_text)
    int2 = get_next_interruption(session1)
    print(f"Q2 (Adaptive): {q2}")
    print(f"Interruption 2 ({int2['type']}): {int2['prompt']}")

    # Candidate answers Q2
    ans2_text = "I structured Django using models for ORM, views for requests, and REST serializers."
    ev2 = ResponseEvaluation.objects.create(
        session=session1,
        question_text=q2,
        transcript_text=ans2_text,
        duration_seconds=18.0,
        words_count=14,
        overall_score=88
    )
    StressAnalysis.objects.create(
        evaluation=ev2,
        is_interrupted=True,
        interruption_prompt=int2['prompt'],
        reaction_time=1.5,
        recovery_time=3.5,
        stress_score=90
    )

    # Q3 Selection
    q3 = select_next_question_for_session(session1, last_transcript=ans2_text)
    int3 = get_next_interruption(session1)
    print(f"Q3: {q3}")
    print(f"Interruption 3 ({int3['type']}): {int3['prompt']}")

    # Candidate answers Q3
    ans3_text = "I debug programs using breakpoints, logging tracebacks, and writing unit tests."
    ev3 = ResponseEvaluation.objects.create(
        session=session1,
        question_text=q3,
        transcript_text=ans3_text,
        duration_seconds=20.0,
        words_count=12,
        overall_score=82
    )

    # Q4 Selection
    q4 = select_next_question_for_session(session1, last_transcript=ans3_text)
    int4 = get_next_interruption(session1)
    print(f"Q4: {q4}")
    print(f"Interruption 4 ({int4['type']}): {int4['prompt']}")

    # Verify session 1 questions & interruptions uniqueness
    assert len(session1.used_questions_json) == 4, f"Expected 4 questions, got {len(session1.used_questions_json)}"
    assert len(session1.used_interruptions_json) == 4, f"Expected 4 interruptions, got {len(session1.used_interruptions_json)}"
    assert len(set(session1.used_interruptions_json)) == 4, "Interruption types MUST NOT repeat in the same session!"
    print("[OK] TEST 1 PASSED: Software Developer Interview 1 completed cleanly with unique interruptions and questions.")

    # --------------------------------------------------
    # TEST 2: Software Developer Interview 2 (Different Sequence Check)
    # --------------------------------------------------
    print("\n--- TEST 2: Software Developer Interview #2 (History Exclusion Check) ---")
    session2 = InterviewSession.objects.create(
        user=user,
        interview_type='adaptive',
        job_role='Software Developer',
        pressure_level='medium',
        used_questions_json=[],
        used_interruptions_json=[]
    )
    
    s2_q1 = select_next_question_for_session(session2)
    s2_int1 = get_next_interruption(session2)
    print(f"Session 2 Q1: {s2_q1}")
    print(f"Session 2 Interruption 1 ({s2_int1['type']}): {s2_int1['prompt']}")

    # Verify Session 2 Q1 is NOT identical or semantically similar to Session 1 Q1!
    assert not check_semantic_similarity(q1, s2_q1), f"Session 2 Q1 '{s2_q1}' is too similar to Session 1 Q1 '{q1}'!"
    print("[OK] TEST 2 PASSED: New interview generated a fresh, distinct question sequence!")

    # --------------------------------------------------
    # TEST 3: Frontend Developer Role Questions
    # --------------------------------------------------
    print("\n--- TEST 3: Frontend Developer Role Questions ---")
    session_fe = InterviewSession.objects.create(
        user=user,
        interview_type='job_role_interview',
        job_role='Frontend Developer',
        pressure_level='medium',
        used_questions_json=[],
        used_interruptions_json=[]
    )
    fe_q1 = select_next_question_for_session(session_fe)
    fe_q2 = select_next_question_for_session(session_fe, last_transcript="I built a responsive web app using React state and CSS flexbox.")
    print(f"Frontend Q1: {fe_q1}")
    print(f"Frontend Q2 (Adaptive): {fe_q2}")
    
    fe_keywords = ["html", "css", "javascript", "dom", "react", "responsive", "frontend", "state", "props"]
    assert any(kw in fe_q1.lower() or kw in fe_q2.lower() for kw in fe_keywords), "Frontend Developer questions must contain frontend domain topics!"
    print("[OK] TEST 3 PASSED: Frontend Developer role questions correctly selected.")

    # --------------------------------------------------
    # TEST 4: Data Analyst Role Questions
    # --------------------------------------------------
    print("\n--- TEST 4: Data Analyst Role Questions ---")
    session_da = InterviewSession.objects.create(
        user=user,
        interview_type='job_role_interview',
        job_role='Data Analyst',
        pressure_level='medium',
        used_questions_json=[],
        used_interruptions_json=[]
    )
    da_q1 = select_next_question_for_session(session_da)
    da_q2 = select_next_question_for_session(session_da, last_transcript="I clean datasets using Pandas and execute SQL inner joins.")
    print(f"Data Analyst Q1: {da_q1}")
    print(f"Data Analyst Q2 (Adaptive): {da_q2}")
    
    da_keywords = ["data", "sql", "cleaning", "join", "missing", "dashboard", "visualization", "table", "null"]
    assert any(kw in da_q1.lower() or kw in da_q2.lower() for kw in da_keywords), "Data Analyst questions must contain data analysis domain topics!"
    print("[OK] TEST 4 PASSED: Data Analyst role questions correctly selected.")

    # --------------------------------------------------
    # TEST 5: Java Developer Role Questions
    # --------------------------------------------------
    print("\n--- TEST 5: Java Developer Role Questions ---")
    session_java = InterviewSession.objects.create(
        user=user,
        interview_type='job_role_interview',
        job_role='Java Developer',
        pressure_level='medium',
        used_questions_json=[],
        used_interruptions_json=[]
    )
    java_q1 = select_next_question_for_session(session_java)
    print(f"Java Developer Q1: {java_q1}")
    
    java_keywords = ["java", "jvm", "heap", "stack", "spring", "collection", "hashmap", "final"]
    assert any(kw in java_q1.lower() for kw in java_keywords), "Java Developer questions must contain Java domain topics!"
    print("[OK] TEST 5 PASSED: Java Developer role questions correctly selected.")

    # --------------------------------------------------
    # TEST 6: Robust Fallback System Check
    # --------------------------------------------------
    print("\n--- TEST 6: Fallback Safety Check (No Null / Empty String / Undefined) ---")
    session_empty = InterviewSession.objects.create(
        user=user,
        interview_type='job_role_interview',
        job_role='Custom AI Engineer Role',
        pressure_level='medium',
        used_questions_json=[],
        used_interruptions_json=[]
    )
    fallback_q = select_next_question_for_session(session_empty)
    assert fallback_q and isinstance(fallback_q, str) and len(fallback_q.strip()) > 5, "Fallback question must be a valid non-empty string!"
    assert fallback_q not in ["null", "undefined", "None", ""], "Fallback must never return null/undefined/empty string!"
    print(f"Fallback Generated Question: '{fallback_q}'")
    print("[OK] TEST 6 PASSED: Fallback system returned valid non-null string.")

    print("\n==================================================")
    print("ALL TESTS PASSED SUCCESSFULLY!")
    print("==================================================")

if __name__ == '__main__':
    run_test_suite()
