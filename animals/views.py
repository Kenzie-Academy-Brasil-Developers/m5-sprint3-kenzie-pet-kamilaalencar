from django.shortcuts import render
from rest_framework.views import APIView, Response, status

from .models import Animal
from .serializers import AnimalSerializer

class AnimalView(APIView):
    def get(self, request):
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many = True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

