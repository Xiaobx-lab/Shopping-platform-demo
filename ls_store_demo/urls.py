"""ls_store_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from goods import views
from ls_store_demo.settings import DEBUG, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^goods/', include('goods.urls')),
    url(r'^api/', include('api.urls')),
    url(r'^user/', include('userapp.urls')),
    url(r'^$', views.Index.as_view()),


    # url(r'^', TemplateView.as_view(template_name='index.html')),
]

if DEBUG:
    from django.views.static import serve
    urlpatterns.append(url(r'media/(.*)',serve,kwargs={'document_root':MEDIA_ROOT}))