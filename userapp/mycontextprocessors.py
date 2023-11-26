#coding=utf-8

def getUserInfo(request):
    return {'user':request.session.get('user',None)}
def getCode(request):
    return {'code':request.session.get('code',None)}