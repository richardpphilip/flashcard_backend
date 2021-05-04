from django.shortcuts import render
from .models import Flashcard
from .serializers import FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class FlashcardList(APIView):
    def get(self, request):
        flashcard = Flashcard.objects.all()
        serializer = FlashcardSerializer(flashcard, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetail(APIView):
    def get_object(self, pk):
        try:
            return Flashcard.objects.get(pk=pk)
        except Flashcard.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        flashcard = self.get_object(pk)
        serializer = FlashcardSerializer(flashcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        flashcard = self.get_object(pk)
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
