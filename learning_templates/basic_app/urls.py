from django.urls import path
from basic_app import views

# from django.conf.urls import url
# from django.contrib import admin
# from basic_app import views

app_name = 'basic_app'

urlpatterns = [
	path('relative/', views.relative, name='index'),
	path('other/', views.other, name='other'),
]


   