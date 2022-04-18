from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Specialty1, Specialty2, Specialty3, SpecialtyStd, UploadModel

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadModel
        fields = '__all__'
    # def create(self, validated_data):
    #     print('hello')

class Specialty3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty3
        fields = (
            'value',
            'label',
            'description'
        )
    def create(self, validated_data):
        print('@Sp3.create()')
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
        print('@Sp2.create()')
        sp1_value = self.context.get("sp1_value")
        if sp1_value:
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
            'specialty2',
        )
    def create(self, validated_data):
        print('@Sp1.create()')
        # print(validated_data)
        sp2s_data = None
        if 'specialty2' in validated_data:
            sp2s_data = validated_data.pop('specialty2')
            # print(sp2s_data)
        sp1_value = validated_data['value']
        # print('specialty1:', sp1_value)
        Specialty1.objects.filter(value=sp1_value).delete() # 删除存在的同value科别
        specialty1 = Specialty1.objects.create(**validated_data)
        # print('specialty1 obj created:', specialty1)
        if sp2s_data:
            for sp2_data in sp2s_data:
                # print(' |—— sp2_data:', sp2_data)
                sp3s_data = None
                if 'specialty3' in sp2_data:
                    sp3s_data = sp2_data.pop('specialty3')
                specialty2 = Specialty2.objects.create(specialty1=specialty1,**sp2_data)
                # print(' |   specialty2 obj created:', specialty2)
                if sp3s_data:
                    for sp3_data in sp3s_data:
                        # print(' | |—— sp3_data:', sp3_data)
                        specialty3 = Specialty3.objects.create(specialty2=specialty2, **sp3_data)
                        # print(' |     specialty3 obj created:', specialty3)
                
        return specialty1
    
class SpecialtyStdSerializer(serializers.ModelSerializer):
    specialty1 = Specialty1Serializer(many=True, required=False)
    class Meta:
        model = SpecialtyStd
        fields = (
            'name',
            'specialty1',
        )
    def create(self, validated_data):
        print('@SpStd.create()')
        # print(validated_data)
        sp1s_data = None
        if 'specialty1' in validated_data:
            sp1s_data = validated_data.pop('specialty1')
            # print(sp1s_data)
        specialtystd = SpecialtyStd.objects.create(**validated_data)
        print('specialtystd obj created:', specialtystd)
        if sp1s_data:
            for sp1_data in sp1s_data:
                # print('sp1_data:', sp1_data)
                sp2s_data = None
                if 'specialty2' in sp1_data:
                    sp2s_data = sp1_data.pop('specialty2')
                    # print('sp1_data after pop:', sp1_data)
                specialty1 = Specialty1.objects.create(specialtystd=specialtystd, **sp1_data)
                # print('specialty1 obj created:', specialty1)
                if sp2s_data:
                    for sp2_data in sp2s_data:
                        # print(' |—— sp2_data:', sp2_data)
                        sp3s_data = None
                        if 'specialty3' in sp2_data:
                            sp3s_data = sp2_data.pop('specialty3')
                        specialty2 = Specialty2.objects.create(specialty1=specialty1,**sp2_data)
                        # print(' |   specialty2 obj created:', specialty2)
                        if sp3s_data:
                            for sp3_data in sp3s_data:
                                # print(' | |—— sp3_data:', sp3_data)
                                specialty3 = Specialty3.objects.create(specialty2=specialty2, **sp3_data)
                                # print(' |     specialty3 obj created:', specialty3)
                
        return specialty1
