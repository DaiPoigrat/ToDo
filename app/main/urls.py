from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('register', include('todo_prev.urls'), name='register'),
    # path('login', include('authorization.urls'), name='login')
]
