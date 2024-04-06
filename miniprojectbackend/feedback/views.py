from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feedback
from .serializers import FeedbackSerializer

class FeedbackList(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self):
        pass
