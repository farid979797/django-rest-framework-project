from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from actors.models import Actors, Category
from actors.permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from actors.serializers import ActorSerializer


class ActorAPIList(generics.ListCreateAPIView):                          # упрощение ActorAPIView, get и post
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ActorAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication, )


class ActorAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAdminOrReadOnly, )
