from django.urls import path
from . import views

urlpatterns = [
    path('feedbacks/', views.FeedbackList.as_view()),
]