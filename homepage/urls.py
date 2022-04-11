from django.urls import path, include

from homepage import views

urlpatterns = [
    path('post-homepage/', views.postForm),
    path('update-homepage/', views.updateForm),
    path('get-homepages/', views.HomepageList.as_view()),
    path('del-homepage/', views.RemoveHomepage.as_view()),
    path('view-homepage/', views.ViewHomepage.as_view()),
]