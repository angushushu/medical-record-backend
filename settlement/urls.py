from django.urls import path, include

from settlement import views

urlpatterns = [
    # path('post-settlement/', views.postForm),
    path('update-settlement/', views.updateForm),
    path('get-settlements/', views.SettlementList.as_view()),
    path('del-settlement/', views.RemoveSettlement.as_view()),
    # path('new-settlement/', views.NewSettlement.as_view()),
    path('view-settlement/', views.ViewSettlement.as_view()),
]