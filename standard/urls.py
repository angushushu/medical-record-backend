from django.urls import path, include

from standard import views

urlpatterns = [
    path('get-standards/', views.StandardList.as_view()),
    path('post-standard/specialty1/', views.postSpecialty1),
    path('post-standard/specialty2/<str:sp1_value>/', views.postSpecialty2),
    path('post-standard/specialty3/<str:sp2_value>/', views.postSpecialty3),
]