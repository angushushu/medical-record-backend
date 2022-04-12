from hashlib import new
from turtle import home
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Specialty1, Specialty2#, Specialty3
from .serializers import Specialty1Serializer, Specialty2Serializer, Specialty3Serializer

from django.db.models import Q # database查询

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