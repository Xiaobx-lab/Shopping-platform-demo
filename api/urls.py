from django.conf.urls import url
from django.urls import path, include

from api import views

urlpatterns = [

    url(r'^$', views.ChatView.as_view()),


    # url(r'^', TemplateView.as_view(template_name='index.html')),
]