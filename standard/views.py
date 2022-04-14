import codecs
from email import message
from hashlib import new
import os
from turtle import home
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

from .models import Specialty1, Specialty2, UploadModel#, Specialty3
from .serializers import UploadSerializer, Specialty1Serializer, Specialty2Serializer, Specialty3Serializer

from django.db.models import Q # database查询

import json
import xmltodict

class UploadViewSet(ModelViewSet):
    queryset = UploadModel.objects.all()
    # serializer_class = UploadSerializer
    # def list(self, request):
    #     return Response("GET API")
    def xml_to_json(xml_str):
        xml_parse=xmltodict.parse(xml_str)
        json_str=json.dumps(xml_parse, indent=1)
        return json_str
    def create(self, request):
        print('UploadViewSet.create()')
        print('request:',request)
        print('request.data:',request.data)
        serializer_class = UploadSerializer(data=request.data)
        print('validation:', serializer_class.is_valid())
        if(serializer_class.is_valid()):
            serializer_class.save()
        file_uploaded = request.FILES.get('file')
        print('file:',file_uploaded)
        content_type = file_uploaded.content_type
        print("POST API: 你一上传了一个{}文件".format(content_type))

        file_dir = str(settings.MEDIA_ROOT)+'\\uploads\\'+str(file_uploaded)
        print(file_dir)
        
        # 取编码并根据编码取值转为dict
        data_dict = None
        encoding = None
        with open(file_dir, 'rb') as f:
            data = f.read()
            encoding = chardet.detect(data)['encoding']
            
            f.close()
        with open(file_dir, 'r', encoding=encoding) as f:
            data = f.read()
            xml_data = ET.fromstring(data) # 直接处理string
            xmlstr = ET.tostring(xml_data, encoding='utf-8', method='xml')
            data_dict = dict(xmltodict.parse(xmlstr))
            print(data_dict)
            f.close()
        print(data_dict[''])
        
            
        response = "POST API: 你一上传了一个{}文件".format(content_type)

        # 砖码并录入

        return Response(response)

@api_view(['POST'])
def postSpecialty1(request):
    data = request.data['form']
    # {
    #     value: '',
    #     label: '',
    #     description: '',
    # }
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

class StandardList(APIView):
    def get(self, request, format=None):
        # page = request.GET.get('page')
        query = request.GET.get('query')
        if query:
            specialty1_list = Specialty1.objects.filter(Q(label__icontains=query)|Q(description__icontains=query))
        else:
            print('obtaining')
            specialty1_list = Specialty1.objects.all()
            print(specialty1_list)
            print(list(specialty1_list))
        # paginator = Paginator(homepage_list, 10)
        # if len(homepage_list) != 0:
        #     print(homepage_list[0])
            # 可再次插入简化过程以降低传输信息量
        # try:
        #     homepages = paginator.page(page)
        # except PageNotAnInteger:
        #     homepages = paginator.page(1)
        # except EmptyPage:
        #     homepages = paginator.page(paginator.num_pages)
        serializer = Specialty1Serializer(specialty1_list, many=True)

        # return Response({'specialty1_list':serializer.data,'total_count':paginator.count})
        return Response({'specialty1_list':serializer.data})