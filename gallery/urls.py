from django.urls import path
from . import views

urlpatterns = [
 path('', views.ImageList.as_view(), name='gallery'),
]
