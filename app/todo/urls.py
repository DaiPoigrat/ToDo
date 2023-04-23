from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('<int:user_id>/today', views.today, name='today'),
    path('<int:user_id>/yesterday', views.yesterday, name='yesterday'),
    # path('<int:user_id>/upcoming', views.upcoming, name='upcoming'),
    path('<int:user_id>/<str:arg>/<int:task_id>/pass', views.passTask, name='passed'),
    path('<int:user_id>/<str:arg>/<int:task_id>/delete', views.deleteTask, name='delete'),
    path('<int:user_id>/<str:arg>/<int:task_id>/edit', views.editTask, name='edit'),
    # path('<int:user_id>/upcoming/<str:selected_day>', views.select_day, name='select'),
    path('<int:user_id>/profile', views.profile, name='profile'),
    path('<int:user_id>/profile/update', views.profile_update, name='update'),
]
