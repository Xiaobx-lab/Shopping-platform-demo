#coding=utf-8

from django.conf.urls import url
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

# from .views import CustomTokenObtainPairView
from userapp import views

urlpatterns=[
    path(r'api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^login/', views.LoginView.as_view()),
    url(r'^register/', views.RegisterView.as_view()),
    url(r'^session-data/', views.getSessionDataView),
    url(r'^session-data-clear/', views.clearSessionDataView),
    url(r'^loadCode/', views.LoadCode.as_view()),
    url(r'^checkCode/', views.checkCode),
    url(r'^testProtected/', views.TestProtected.as_view()),
]