from django.urls import path
from booktest import views
#index
urlpatterns = [
    path('index', views.index),
    # 建立/index和视图index之间的关系
    path('index2', views.index2)
]