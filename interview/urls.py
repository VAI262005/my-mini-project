from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # 3 MAIN PAGES
    path('', views.ai_interview_view, name='home'),
    path('ai-interview/', views.ai_interview_view, name='ai_interview'),
    path('resume-analyzer/', views.resume_analyzer_view, name='resume_analyzer'),
    path('learning-center/', views.learning_center_view, name='learning_center'),
    
    # Internal Redirect Alias Mappings for Backward Compatibility
    path('select/', views.ai_interview_view, name='select_interview'),
    path('hr-prep/', views.ai_interview_view, name='hr_interview'),
    path('technical-prep/', views.ai_interview_view, name='technical_interview'),
    path('performance/', views.ai_interview_view, name='performance_dashboard'),
    
    # Auth
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    
    # Password Reset
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    
    # Session Management & Execution API
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('progress/', views.progress_view, name='progress'),
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
    path('start/<str:track>/', views.start_interview_view, name='start_interview'),
    path('room/<int:session_id>/', views.interview_room_view, name='interview_room'),
    path('api/process_answer/', views.process_answer_api, name='process_answer_api'),
    path('api/learning/toggle_complete/', views.toggle_learning_complete_api, name='toggle_learning_complete_api'),
    path('api/learning/toggle_bookmark/', views.toggle_learning_bookmark_api, name='toggle_learning_bookmark_api'),
    path('api/learning/submit_quiz/', views.submit_learning_quiz_api, name='submit_learning_quiz_api'),
    path('video-analysis/', views.video_analysis_view, name='video_analysis'),
    path('result/<int:session_id>/', views.result_view, name='result'),
    path('report/<int:session_id>/', views.report_detail_view, name='report_detail'),
    path('report/<int:session_id>/pdf/', views.download_pdf_view, name='download_pdf'),
]
