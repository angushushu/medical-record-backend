from posixpath import basename
from django.urls import path, include
from rest_framework import routers
from standard import views

# upload = views.UploadViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
router = routers.DefaultRouter()
router.register(r'upload-std/json-sp', views.UploadJsonViewSet, basename='upload-json-sp')
router.register(r'upload-std/xls-sp', views.UploadXlsViewSet, basename='upload-xls-sp')
router.register(r'upload-std/json-dg', views.UploadDgJsonViewSet, basename='upload-json-dg')
router.register(r'upload-std/xls-dg', views.UploadDgXlsViewSet, basename='upload-xls-dg')
router.register(r'upload-std/json-g', views.UploadGJsonViewSet, basename='upload-json-g')
router.register(r'upload-std/xls-g', views.UploadGXlsViewSet, basename='upload-xls-g')

urlpatterns = [
    # path('get-standards/', views.StandardList.as_view()),
    # 科室标准
    path('get-spstd/', views.ViewSpStd.as_view()),
    path('get-spstds/', views.SpStdList.as_view()),
    path('upload-std/json-example', views.getJsonExample),
    path('upload-std/xls-example', views.getXlsExample),
    path('upload-std/xlsx-example', views.getXlsxExample),
    path('upload-std/dg-json-example', views.getDgJsonExample),
    path('upload-std/dg-xls-example', views.getDgXlsExample),
    path('upload-std/dg-xlsx-example', views.getDgXlsxExample),
    path('get-standard/specialty/', views.getAppliedSpStd),
    path('set-standard/specialty/', views.setAppliedSpStd),
    path('post-standard/specialty/', views.postSpecialtyStd),
    path('post-standard/specialty1/', views.postSpecialty1),
    path('post-standard/specialty2/<str:sp1_value>/', views.postSpecialty2),
    path('post-standard/specialty3/<str:sp2_value>/', views.postSpecialty3),
    path('update-standard/specialty/', views.updateSpecialtyStd),
    path('remove-spstd', views.removeSpecialtyStd),

    # dgstd
    path('get-dgstd/', views.ViewDgStd.as_view()),
    path('get-dgstds/', views.DgStdList.as_view()),
    path('query-diag/',views.DiagQuery.as_view()),
    path('get-standard/dgstd/', views.getAppliedDgStd),
    path('set-standard/dgstd/', views.setAppliedDgStd),
    path('post-standard/dgstd/', views.postDiagStd),
    path('post-standard/diag/', views.postDiag),
    path('update-standard/dgstd/', views.updateDiagStd),
    path('remove-dgstd', views.removeDiagStd),
    # path('upload-standards/', upload, name='upload'),
    path('', include(router.urls)),

    # gstd
    path('get-standard/gstd/', views.getAppliedGStd), # get applied gstd of certain type
    path('get-standard/gstds', views.getAppliedGStds), # get all applied gstds with type
    path('set-standard/gstd/', views.setAppliedGStd), # set applied gstd of certain type
    path('get-gstd/', views.ViewGStd.as_view()),
    path('get-gstds/', views.GStdList.as_view()),
    path('get-all-gstds/', views.AllGStdList.as_view()),
    path('post-standard/gstd/', views.postGStd),
    path('update-standard/gstd/', views.updateGStd),
    path('post-standard/general/', views.postGeneral), # 似乎没用
    path('remove-gstd', views.removeGStd),
    path('get-type-name', views.getTypeName),

    # g2std
    path('get-standard/g2std/', views.getAppliedG2Std), # get applied g2std of certain type
    path('get-standard/g2stds', views.getAppliedG2Stds), # get all applied gstds with type
    path('set-standard/g2std/', views.setAppliedG2Std), # set applied gstd of certain type
    path('get-g2std/', views.ViewG2Std.as_view()),
    path('get-g2stds/', views.G2StdList.as_view()),
    path('get-all-g2stds/', views.AllG2StdList.as_view()),
    path('post-standard/g2std/', views.postG2Std),
    path('update-standard/g2std/', views.updateG2Std),
    path('remove-g2std', views.removeG2Std)
]