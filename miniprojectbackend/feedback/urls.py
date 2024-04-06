from django import path
from . import views

urlpatterns = [
    path('feedbacks/', views.FeedbackList.as_view()),
]