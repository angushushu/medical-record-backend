from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import Diag, DiagStd, G2Std, GStd, General, General1, General2, Specialty1, Specialty2, Specialty3, SpecialtyStd, UploadModel

class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadModel
        fields = '__all__'
    # def create(self, validated_data):
    #     print('hello')

class General2Serializer(serializers.ModelSerializer):
    class Meta:
        model = General2
        fields = (
            'value',
            'label'
        )
    def create(self, validated_data):
        print('@General2.create()')
        g1_value = self.context.get("g1_value")
        if g1_value:
            print('general1:', g1_value)
            general1 = General1.objects.get(value=g1_value)
        print('general1 obj:', general1)
        general2 = General2.objects.create(general1=general1, **validated_data)
        print('general2 obj:', general1)
        return general2

class General1Serializer(serializers.ModelSerializer):
    general2 = General2Serializer(many=True, required=False)
    class Meta:
        model = General1
        fields = (
            'value',
            'label',
            'general2'
        )
    def create(self, validated_data):
        print('@General1.create()')
        g1_value = self.context.get("g1_value")
        sp2s_data = None
        if 'general2' in validated_data:
            g2s_data = validated_data.pop('general2')
        g1_value = validated_data['value']
        General1.objects.filter(value=g1_value).delete() # 删除存在的同value科别
        general1 = General1.objects.create(**validated_data)
        if g2s_data:
            for g2_data in g2s_data:
                general2 = General2.objects.create(general1=general1,**g2_data)
        return general1

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

class G2StdSerializer(serializers.ModelSerializer):
    general1 = General1Serializer(many=True, required=False)
    type = serializers.ChoiceField(choices=G2Std.Type)
    id = -1
    class Meta:
        model = G2Std
        fields = (
            'id',
            'name',
            'general1',
            'type'
        )
    def create(self, validated_data):
        print('@G2StdSerializer.create()')
        g1s_data = None
        if 'general1' in validated_data:
            g1s_data = validated_data.pop('general1')
        g2std = G2Std.objects.create(**validated_data)
        print('g2std obj created:', g2std)
        if g1s_data:
            for g1_data in g1s_data:
                g2s_data = None
                if 'general2' in g1_data:
                    g2s_data = g1_data.pop('general2')
                general1 = General1.objects.create(g2std=g2std, **g1_data)
                if g2s_data:
                    for g2_data in g2s_data:
                        general2 = General2.objects.create(general1=general1,**g2_data)      
        return g2std
    
    def update(self, instance, validated_data):
        print('@G2StdSerializer.update()')
        instance.name = validated_data.get('name', instance.name)
        print('changing name to',validated_data['name'])
        General1.objects.filter(g2std=instance).delete()
        g1s_data = None
        if 'general1' in validated_data:
            g1s_data = validated_data.pop('general1')
        if g1s_data:
            for g1_data in g1s_data:
                print('g1_data:', g1_data)
                g2s_data = None
                if 'general2' in g1_data:
                    g2s_data = g1_data.pop('general2')
                    print('g1_data after pop:', g1_data)
                general1 = General1.objects.create(g2std=instance, **g1_data)
                if g2s_data:
                    for g2_data in g2s_data:
                        General2.objects.create(general1=general1,**g2_data)
        instance.save()
        return instance

class SpecialtyStdSerializer(serializers.ModelSerializer):
    specialty1 = Specialty1Serializer(many=True, required=False)
    id = -1
    class Meta:
        model = SpecialtyStd
        fields = (
            'id',
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
                
        return specialtystd
    
    def update(self, instance, validated_data):
        print('SpecialtyStdSerializer.update()')
        instance.name = validated_data.get('name', instance.name)
        print('changing name to',validated_data['name'])
        Specialty1.objects.filter(specialtystd=instance).delete()
        sp1s_data = None
        if 'specialty1' in validated_data:
            sp1s_data = validated_data.pop('specialty1')
            # print(sp1s_data)
        if sp1s_data:
            for sp1_data in sp1s_data:
                print('sp1_data:', sp1_data)
                sp2s_data = None
                if 'specialty2' in sp1_data:
                    sp2s_data = sp1_data.pop('specialty2')
                    print('sp1_data after pop:', sp1_data)
                specialty1 = Specialty1.objects.create(specialtystd=instance, **sp1_data)
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
        instance.save()
        return instance

class DiagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diag
        fields = (
            'code',
            'label',
            'pinyin',
            'pinyin_cap',
            'description',
        )
    def create(self, validated_data):
        print('@Diag.create()')
        print(validated_data)
        diag_code = validated_data['code']
        print('diag:', diag_code)
        existed = Diag.objects.filter(code__exact=diag_code) # 存在的
        if len(existed)>0:
            return existed[0]
        diag = Diag.objects.create(**validated_data)
        print('diag obj created:', diag)
                
        return diag
    
class DiagStdSerializer(serializers.ModelSerializer):
    diag = DiagSerializer(many=True, required=False)
    id = -1
    class Meta:
        model = DiagStd
        fields = (
            'id',
            'name',
            'diag',
        )
    def create(self, validated_data):
        print('@DiagStd.create()')
        print(validated_data)
        diags_data = None
        if 'diag' in validated_data:
            diags_data = validated_data.pop('diag')
        dgstd = DiagStd.objects.create(**validated_data)
        print('dgstd obj created:', dgstd)
        if diags_data:
            for diag_data in diags_data:
                print('diag_data:', diag_data)
                Diag.objects.create(diagstd=dgstd, **diag_data)
        return dgstd
    
    def update(self, instance, validated_data):
        print('@DiagStdSerializer.update()')
        instance.name = validated_data.get('name', instance.name)
        print('changing name to',validated_data['name'])
        Diag.objects.filter(diagstd=instance).delete()
        if 'diag' in validated_data:
            diags_data = validated_data.pop('diag')
            for diag_data in diags_data:
                print('diag_data:', diag_data)
                Diag.objects.create(diagstd=instance, **diag_data)
        instance.save()
        return instance

class GeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = General
        fields = (
            'code',
            'label',
        )
    def create(self, validated_data):
        print('@GeneralSerializer.create()')
        print(validated_data)
        code = validated_data['code']
        print('general:', code)
        existed = General.objects.filter(code__exact=code) # 存在的
        if len(existed)>0:
            return existed[0]
        general = General.objects.create(**validated_data)
        print('general obj created:', general)
                
        return general

class GStdSerializer(serializers.ModelSerializer):
    general = GeneralSerializer(many=True, required=True)
    type = serializers.ChoiceField(choices=GStd.Type)
    id = -1
    class Meta:
        model = GStd
        fields = (
            'id',
            'name',
            'general',
            'type'
        )
    def create(self, validated_data):
        print('@GeneralStdSerializer.create()')
        print(validated_data)
        generals_data = None
        if 'general' in validated_data:
            generals_data = validated_data.pop('general')
            print('generals_data:',generals_data)
        gstd = GStd.objects.create(**validated_data)
        print('gstd obj created:', gstd)
        if generals_data:
            for general_data in generals_data:
                print('general_data:', general_data)
                General.objects.create(gstd=gstd, **general_data)
        return gstd
    
    def update(self, instance, validated_data):
        print('@GeneralStdSerializer.update()')
        instance.name = validated_data.get('name', instance.name)
        print('changing name to',validated_data['name'])
        General.objects.filter(gstd=instance).delete()
        if 'general' in validated_data:
            generals_data = validated_data.pop('general')
            for general_data in generals_data:
                print('general_data:', general_data)
                General.objects.create(gstd=instance, **general_data)
        instance.save()
        return instance