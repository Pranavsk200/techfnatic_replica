from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard,name='index'),
    path('adminRep', views.adminRep,name='adminRep'),
    path('adminRep/product', views.adminProductDis, name='adminProductDis'),
    path('adminRep/settings', views.websiteSettings, name='settings'),
    path('adminRep/login', views.login, name='login'),
    path('logout', views.log_out, name="logout")
]

