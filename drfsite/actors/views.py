from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from actors.models import Actors
from actors.serializers import ActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

# class ActorAPIList(generics.ListCreateAPIView):                          # упрощение ActorAPIView, get и post
#     queryset = Actors.objects.all()
#     serializer_class = ActorSerializer
#
#
# class ActorAPIUpdate(generics.UpdateAPIView):
#     queryset = Actors.objects.all()
#     serializer_class = ActorSerializer
#
#
# class ActorAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Actors.objects.all()
#     serializer_class = ActorSerializer
