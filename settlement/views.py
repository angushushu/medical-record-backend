from urllib import response
from xmlrpc.client import ResponseError
from django.shortcuts import render
from homepage.models import Homepage
from homepage.serializers import HomepageSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from settlement.models import Settlement

from .serializers import SettlementSerializer

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger # 分页用
from django.db.models import Q # database查询

# Create your views here.
# @api_view(['POST'])
# def postForm(request):
#     data = request.data['form']
#     print('data:',data)
    
#     settlement_serializer = SettlementSerializer(data=data)
#     # print(homepage.settlement)
#     if settlement_serializer.is_valid():
#         print('valid')
#         settlement_serializer.save()
#     else:
#         print(settlement_serializer.errors)
#     print('giao')
#     return Response({"request.data":request.data})

@api_view(['POST'])
def updateForm(request):
    print('---- updateForm ----')
    data = request.data['form']
    homepage_id = data['homepage_id']
    print('--update--')
    print('request.data:',data)
    print('homepage_id:',homepage_id)
    # has settle
    # no settle
    settlements = Settlement.objects.filter(homepage_id=homepage_id)
    if len(settlements) == 0:
        print('---- create a settlement ----')
        settlement_serializer = SettlementSerializer(data=data)
        if settlement_serializer.is_valid():
            print('valid')
            settlement_serializer.save()
        else:
            print(settlement_serializer.errors)
        print('---- giao ----')
        return Response({"request.data":request.data})
    else:
        settlement = settlements[0]
        settlement_serializer = SettlementSerializer(settlement, data)
        print(settlements)
        print('settlement valid:',settlement_serializer.is_valid())
        if settlement_serializer.is_valid():
            # print(homepage_serializer.validated_data)
            settlement_serializer.save()
        else:
            print(settlement_serializer.errors)
        print('giao')
        return Response({"request.data":request.data})

class SettlementList(APIView):
    def get(self, request, format=None):
        page = request.GET.get('page')
        query = request.GET.get('query')
        if query:
            settlement_list = Settlement.objects.filter(Q(org_name__icontains=query)|Q(org_code__icontains=query))
        else:
            settlement_list = Settlement.objects.all()
        paginator = Paginator(settlement_list, 10)
        # print('page', page)
        # print('query', query)
        if len(settlement_list) != 0:
            print(settlement_list[0])
            # 可再次插入简化过程以降低传输信息量
        try:
            homepages = paginator.page(page)
        except PageNotAnInteger:
            homepages = paginator.page(1)
        except EmptyPage:
            homepages = paginator.page(paginator.num_pages)
        serializer = SettlementSerializer(homepages, many=True)
        # print('list-data:',serializer.data)

        print('count',paginator.count)
        # print(serializer.data)
        return Response({'settlements':serializer.data,'total_count':paginator.count})

class RemoveSettlement(APIView):
    def get(self, request, format=None):
        homepage_id = request.GET.get('homepage_id')
        print('got homepage_id:', homepage_id)
        settlement = Settlement.objects.get(homepage_id__exact=homepage_id)
        if settlement:
            settlement.delete()
        return Response()

class ViewSettlement(APIView):
    def get(self, request, format=None):
        print('ViewSettlement')
        homepage_id = request.GET.get('homepage_id')
        new = request.GET.get('new')
        print('homepage_id:', homepage_id)
        print('new:', new)
        homepages = Homepage.objects.filter(id__exact=homepage_id)
        print(homepages)
        print('looking for settle w/ homepage_id:', homepage_id)
        settlements = Settlement.objects.filter(homepage_id__exact=homepage_id)
        print(settlements)
        response = None
        if len(homepages)!=0:
            print('got homepage', homepages[0])
            if new == 'true' or len(settlements)==0:
                print('  no settlement', settlements)
                response = HomepageSerializer(homepages[0], many=False).data
                # transfer homepage to settlement
                response['list_sn'] = ''
            else:
                print('  got settlement', settlements[0])
                response = SettlementSerializer(settlements[0], many=False).data
        else:
            print('no homepage', homepages)
            response = ResponseError()
        print('new:', new)
        print('type(new)', type(new))
        if new == 'true':
            response['overwrite'] = True
        else:
            response['overwrite'] = False
        print(response)
        
        return Response({'settlement':response})

# class NewSettlement(APIView):
#     def get(self, request, format=None):
#         print('ViewSettlement')
#         homepage_id = request.GET.get('homepage_id')
#         print('viewing w/ homepage_id:', type(homepage_id))
#         print('looking for homepage w/ id:', homepage_id)
#         homepages = Homepage.objects.filter(id__exact=homepage_id)
#         print(homepages)
#         print('looking for settle w/ homepage_id:', homepage_id)
#         settlements = Settlement.objects.filter(homepage_id__exact=homepage_id)
#         print(settlements)
#         response = None
#         if len(homepages)!=0:
#             print('got homepage', homepages[0])
#             response = HomepageSerializer(homepages[0], many=False).data
#             # transfer homepage to settlement
#             response['list_sn'] = ''
#         else:
#             print('no homepage', homepages)
#             response = ResponseError()
#         print(response)
        
#         return Response({'settlement':response})