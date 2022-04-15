from django.urls import path, include
from rest_framework import routers
from standard import views

# upload = views.UploadViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
router = routers.DefaultRouter()
router.register(r'upload-standards', views.UploadViewSet, basename='upload')

urlpatterns = [
    path('get-standards/', views.StandardList.as_view()),
    path('post-standard/specialty/', views.postSpecialtyStd),
    path('post-standard/specialty1/', views.postSpecialty1),
    path('post-standard/specialty2/<str:sp1_value>/', views.postSpecialty2),
    path('post-standard/specialty3/<str:sp2_value>/', views.postSpecialty3),
    # path('upload-standards/', upload, name='upload'),
    path('', include(router.urls)),
]