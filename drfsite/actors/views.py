from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from actors.models import Actors
from actors.serializers import ActorSerializer


class ActorAPIView(APIView):
    def get(self, request):
        w = Actors.objects.all()                                    #.values для набора конкретных значений
        return Response({'posts': ActorSerializer(w, many=True).data})

    def post(self, request):
        serializer = ActorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)                          #проверка валидности полученных данных
        serializer.save()                                                   #вызывает create from serializers.py

        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = Actors.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = ActorSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()                                                       #update from serializers.py
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        try:
            instance = Actors.objects.get(pk=pk).delete()
        except:
            return Response({"error": "Object does not exists"})

        instance.save()
        return Response({"post": "delete post " + str(pk)})

# class ActorAPIView(generics.ListAPIView):
#     queryset = Actors.objects.all()
#     serializer_class = ActorSerializer
