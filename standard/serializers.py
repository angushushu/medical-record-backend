from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Specialty1, Specialty2, Specialty3

class Specialty3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty3
        fields = (
            'value',
            'label',
            'description'
        )
    def create(self, validated_data):
        print('arrived sp3 serializer')
        sp2_value = self.context.get("sp2_value")
        print('specialty2:', sp2_value)
        specialty2 = Specialty2.objects.get(value=sp2_value)
        print('specialty2 obj:', specialty2)
        specialty3 = Specialty3.objects.create(specialty2=specialty2,**validated_data)
        print('specialty3 obj:', specialty3)
        return specialty3

class Specialty2Serializer(serializers.ModelSerializer):
    specialty3 = Specialty3Serializer(many=True, required=False)
    class Meta:
        model = Specialty2
        fields = (
            'value',
            'label',
            'description',
            'specialty3'
        )
    def create(self, validated_data):
        sp1_value = self.context.get("sp1_value")
        print('specialty1:', sp1_value)
        specialty1 = Specialty1.objects.get(value=sp1_value)
        print('specialty1 obj:', specialty1)
        specialty2 = Specialty2.objects.create(specialty1=specialty1,**validated_data)
        print('specialty2 obj:', specialty2)
        return specialty2
    # def update():
    #     print('hushu is a shnooby')

class Specialty1Serializer(serializers.ModelSerializer):
    specialty2 = Specialty2Serializer(many=True, required=False)
    class Meta:
        model = Specialty1
        fields = (
            'value',
            'label',
            'description',
            'specialty2'
        )

