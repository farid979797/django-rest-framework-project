from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from actors.models import Actors, Category
from actors.serializers import ActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    #queryset = Actors.objects.all()
    serializer_class = ActorSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        if not pk:
            return Actors.objects.all()
        return Actors.objects.filter(pk=pk)

    @action(methods=['get'], detail=True)                                                 #добавление нового маршрута в класс ActorViewSet
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

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
