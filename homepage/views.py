from hashlib import new
from turtle import home
from django.http import Http404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Homepage, MainDiag
from .serializers import HomepageSerializer, MainDiagSerializer

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 分页用
from django.db.models import Q # database查询

@api_view(['POST'])
def postForm(request):
    data = request.data['form']
    # print('data', data)
    # 对data做分组处理
    new_data = data
    print(1)
    new_data['other_diags'] = new_data.pop('other_diagnosis')
    print(2)
    print(new_data['admit_specialty'])
    print(new_data['trans_specialty'])
    print(new_data['release_specialty'])
    new_data['ops'] = new_data.pop('operations')
    print(3)
    new_data['main_diag'] = new_data.pop('main_diagnosis')
    print('main_diag:',new_data['main_diag'])
    print('lesion_reason:',new_data['lesion_reason'])
    # print('pathology:',new_data['pathology'])
    
    homepage_serializer = HomepageSerializer(data=new_data)
    print('homepage valid:',homepage_serializer.is_valid())
    if homepage_serializer.is_valid():
        # print(homepage_serializer.validated_data)
        homepage_serializer.save()
    else:
        print(homepage_serializer.errors)
    print('giao')
    
    return Response({"request.data":request.data})

@api_view(['POST'])
def updateForm(request):
    data = request.data['form']
    id = data['id']
    print('id:',id)
    instance = Homepage.objects.get(id=id)
    print(instance)
    
    homepage_serializer = HomepageSerializer(instance, data)
    print('homepage valid:',homepage_serializer.is_valid())
    if homepage_serializer.is_valid():
        # print(homepage_serializer.validated_data)
        homepage_serializer.save()
    else:
        print(homepage_serializer.errors)
    print('giao')
    
    return Response({"request.data":request.data})
    

class HomepageList(APIView):
    def get(self, request, format=None):
        page = request.GET.get('page')
        query = request.GET.get('query')
        if query:
            homepage_list = Homepage.objects.filter(Q(org_name__icontains=query)|Q(org_code__icontains=query))
        else:
            homepage_list = Homepage.objects.all()
        paginator = Paginator(homepage_list, 10)
        # print('page', page)
        # print('query', query)
        if len(homepage_list) != 0:
            print(homepage_list[0])
            # 可再次插入简化过程以降低传输信息量
        try:
            homepages = paginator.page(page)
        except PageNotAnInteger:
            homepages = paginator.page(1)
        except EmptyPage:
            homepages = paginator.page(paginator.num_pages)
        serializer = HomepageSerializer(homepages, many=True)
        # print('list-data:',serializer.data)

        print('count',paginator.count)
        # print(serializer.data)
        return Response({'homepages':serializer.data,'total_count':paginator.count})

class RemoveHomepage(APIView):
    def get(self, request, format=None):
        id = request.GET.get('id')
        print('got id:', id)
        page = Homepage.objects.get(id__exact=id)
        if page:
            page.delete()
        # Homepage.objects.all().delete()
        return Response()

class ViewHomepage(APIView):
    def get(self, request, format=None):
        id = request.GET.get('id')
        print('viewing w/ id:', id)
        page = Homepage.objects.get(id__exact=id)
        print(page.id)
        serializer = HomepageSerializer(page, many=False)

        print('release_specialty:',serializer.data['release_specialty'])

        
        print('response:')
        print('data-main_diag:',serializer.data['main_diag'])
        print('data-main_diag:',serializer.data['other_diags'])
        return Response({'homepage':serializer.data})

