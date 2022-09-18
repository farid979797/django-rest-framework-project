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

        post_new = Actors.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        return Response({'post': ActorSerializer(post_new).data})



# class ActorAPIView(generics.ListAPIView):
#     queryset = Actors.objects.all()
#     serializer_class = ActorSerializer
