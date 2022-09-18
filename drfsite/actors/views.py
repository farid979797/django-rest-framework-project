from django.shortcuts import render
from rest_framework import generics

from actors.models import Actors
from actors.serializers import ActorSerializer


class ActorAPIView(generics.ListAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
