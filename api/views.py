from django.shortcuts import render

#Personal imports 
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room


#Endpoints section

def main(request):
    return HttpResponse("Hello from Django!")






class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
