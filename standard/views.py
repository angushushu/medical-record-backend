import codecs
from email import message
from hashlib import new
import os
from turtle import home
from unicodedata import name
from xml.dom import minidom
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from rest_framework.viewsets import ModelViewSet
from django.conf import settings
import xml.etree.ElementTree as ET
import chardet

from .models import Specialty1, Specialty2, SpecialtyStd, UploadModel#, Specialty3
from .serializers import SpecialtyStdSerializer, UploadSerializer, Specialty1Serializer, Specialty2Serializer, Specialty3Serializer

from django.db.models import Q # database查询

import json
import xmltodict

class UploadJsonViewSet(ModelViewSet):
    queryset = UploadModel.objects.all()
    def create(self, request):
        file_dir = None # 文件存储路径
        json_str = None # 读取的json
        
        print('UploadViewSet.create()')
        # print('request:',request)
        # print('request.data:',request.data)
        upload_serializer = UploadSerializer(data=request.data)
        print('validation:', upload_serializer.is_valid())
        if(upload_serializer.is_valid()):
            upload = upload_serializer.save()
        # file_uploaded = request.FILES.get('file')
        # print('type:', type(file_uploaded))
        # print('file:',file_uploaded)
        # content_type = file_uploaded.content_type
        # print("POST API: 你一上传了一个{}文件".format(content_type))
        file_name = str(upload.file).split('/')[1]
        file_dir = str(settings.MEDIA_ROOT)+'\\uploads\\'+file_name
        print('file_dir:', file_dir)
        # 打开json文件
        json_str = None
        with open(file_dir, encoding = 'utf-8') as f:
            json_str = json.load(f)
        if json_str:
            json_str['name'] = file_name
            # print(json_str)
            specialtystd_serializer = SpecialtyStdSerializer(data=json_str)
            print('validation:', specialtystd_serializer.is_valid())
            if specialtystd_serializer.is_valid():
                specialtystd_serializer.save()
            else:
                print(specialtystd_serializer.errors)
            print('giao')
        
        # 针对.xml取编码并根据编码取值转为dict
        # data_dict = None
        # encoding = None
        # with open(file_dir, 'rb') as f:
        #     data = f.read()
        #     encoding = chardet.detect(data)['encoding']
        #     f.close()
        # with open(file_dir, 'r', encoding=encoding) as f:
        #     data = f.read()
        #     xml_data = ET.fromstring(data) # 直接处理string
        #     xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')
        #     data_dict = dict(xmltodict.parse(xmlstr))
        #     print(data_dict)
        #     f.close()
        # print(data_dict[''])
        
            
        response = "POST API: 你一上传了一个文件:{}".format(file_name)

        # 砖码并录入

        return Response(response)

@api_view(['POST'])
def postSpecialtyStd(request, format=None):
    data = request.data['form']
    print('data:', data)
    specialtystd_serializer = SpecialtyStdSerializer(data=data)
    print('validation:', specialtystd_serializer.is_valid())
    if specialtystd_serializer.is_valid():
        specialtystd_serializer.save()
    else:
        print(specialtystd_serializer.errors)
    print('giao')
    return Response({"request.data":request.data})

@api_view(['POST'])
def postSpecialty1(request, format=None):
    data = request.data['form']
    # {
    #     value: '',
    #     label: '',
    #     description: '',
    #     specialty2
    # }
    print('data:',data)
    specialty1_serializer = Specialty1Serializer(data=data)
    print('validation:',specialty1_serializer.is_valid())
    if specialty1_serializer.is_valid():
        specialty1_serializer.save()
    else:
        print(specialty1_serializer.errors)
    print('giao')
    
    return Response({"request.data":request.data})

@api_view(['POST'])
def postSpecialty2(request, sp1_value, format=None):
    data = request.data['form']
    specialty2_serializer = Specialty2Serializer(data=data, context={"sp1_value":sp1_value})
    print('validation:',specialty2_serializer.is_valid())
    if specialty2_serializer.is_valid():
        specialty2_serializer.save()
    else:
        print(specialty2_serializer.errors)
    print('giao')
    
    return Response({"request.data":request.data})

@api_view(['POST'])
def postSpecialty3(request, sp2_value, format=None):
    data = request.data['form']
    print('going to sp3 serializer')
    specialty3_serializer = Specialty3Serializer(data=data, context={"sp2_value":sp2_value})
    if specialty3_serializer.is_valid():
        specialty3_serializer.save()
    else:
        print(specialty3_serializer.errors)

    return Response({"request.data":request.data})

@api_view(['POST'])
def updateSpecialtyStd(request):
    data = request.data
    # print(data)
    print('name:', data['name'])
    print('spstd:',SpecialtyStd.objects.all())
    # instance = SpecialtyStd.objects.get(name=name)
    instance = SpecialtyStd.objects.get(name__exact=data['name'])
    print('instance:',instance)
    # instance.delete()
    specialtystd_serializer = SpecialtyStdSerializer(instance, data)
    print('new spstd valid:',specialtystd_serializer.is_valid())
    if specialtystd_serializer.is_valid():
        specialtystd_serializer.save()
    else:
        print(specialtystd_serializer.errors)
    print('giao')
    
    return Response({"request.data":request.data})

class ViewSpStd(APIView):
    def get(self, request, format=None):
        name = request.GET.get('name')
        print('spstd w/ name:', name)
        stand = SpecialtyStd.objects.get(name__exact=name)
        print(stand.name)
        serializer = SpecialtyStdSerializer(stand, many=False)

        return Response({'spstd':serializer.data})

class SpStdList(APIView):
    def get(self, request, format=None):
        print('@getSpStdList()')
        spstd_list = SpecialtyStd.objects.all()
        # print(spstd_list)
        serializer = SpecialtyStdSerializer(spstd_list, many=True)
        # print(serializer.data)
        return Response({'spstd_list':serializer.data})
