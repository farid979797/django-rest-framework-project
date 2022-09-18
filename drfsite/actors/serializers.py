import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from actors.models import Actors


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actors
        fields = "__all__"






# def encode():                                                  #выполняются те же действия что указаны в views.py в функции get
#     model = ActorModel('Vitya', 'Content: Geniy jizni')
#     model_sr = ActorSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Vitya", "content":"Content: Geniy jizni"}')
#     data = JSONParser().parse(stream)
#     serializer = ActorSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
