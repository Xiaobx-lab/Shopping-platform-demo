import hashlib
import json

from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View
# Create your views here.
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from userapp.models import UserInfo
from userapp.mycontextprocessors import getUserInfo, getCode
from utils.code import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


def checkUserName(username):
    user = User.objects.filter(username=username)
    if user.exists():  # 如果非空
        flag = False
    else:
        flag = True
    return flag

class RegisterView(View):
    def get(self,request):
        print('enter get sucessfully!')

        return HttpResponse('hhh')

    def post(self,request):

        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        flag = checkUserName(username)  # 用户名唯一校验
        print("flag:",flag)
        if flag:
            # 插入数据库
            # user = UserInfo.objects.create(uname=username,pwd=password)
            hashed_password = make_password(password)
            user = User.objects.create(username=username, password=hashed_password,is_active=True)
            user_data = {
                'uname': user.username,
                'pwd': user.password,
                # 其他字段...
            }
            # 判断是否注册成功
            if user:
                # 将用户信息存储到session对象当中去
                request.session['user'] = user_data

        data = {
            "flag" : flag
        }
        return JsonResponse(data,safe=False, content_type='application/json; charset=utf-8', json_dumps_params={'ensure_ascii': False})

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:  # 如果非空
            print("登陆成功！")
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return JsonResponse({"login_flag":"True",
                                  "token":token
                                  })
        else:
            return JsonResponse({'login_flag':"False"})




def getSessionDataView(request):
    return JsonResponse(getUserInfo(request))

# 删除session中的用户信息
def clearSessionDataView(request):
    if 'user' in request.session:
        del request.session['user']
    return JsonResponse({'del_flag':True})


class LoadCode(View):
    def get(self, request):
        img, str = gene_code()
        request.session['code'] = str
        return HttpResponse(img, content_type='image/png')


def checkCode(request):
    return JsonResponse(getCode(request))


class TestProtected(APIView):
    permission_classes = [permissions.IsAuthenticated]  # 要求身份验证才能访问该API

    def get(self, request):
        user = request.user  # 访问当前已验证的用户
        data = {
            'message': 'You have accessed the protected API.',
            'user': user.username  # 返回当前用户的用户名
        }
        return Response(data)
