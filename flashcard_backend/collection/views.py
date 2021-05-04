from django.shortcuts import render
from .models import Collection
from .serializers import CollectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class CollectionList(APIView):
    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionDetail(APIView):
    def get_object(self, pk):
        try:
            return Collection.objects.get(pk=pk)
        except Collection.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        collection = self.get_object(pk)
        serializer =CollectionSerializer(collection)
        return Response(serializer.data)

    def put(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        collection = self.get_object(pk)
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
