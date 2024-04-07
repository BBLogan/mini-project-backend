from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Feedback
from .serializers import FeedbackSerializer
from django.http import Http404
from rest_framework import status

class FeedbackList(APIView):
    def get(self, request):
        feedbacks = Feedback.objects.all()
        serializer = FeedbackSerializer(feedbacks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data, 
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST
            )

class FeedbackDetail(APIView):
    def get_object(self, pk):
        try:
            return Feedback.objects.get(pk=pk)
        except Feedback.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        feedback = self.get_object(pk)
        serializer = FeedbackSerializer(feedback)
        return Response(serializer.data)
