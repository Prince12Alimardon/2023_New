from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view()),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
