from django.http import HttpResponse
from django.shortcuts import render

from user.views import sign_up_view

def base_response(request):
    return HttpResponse("안녕하세요! 장고의 시작입니다!")

def first_view(request):
    return render(request, 'index.html')




# class User:
#     def sign_up_view(request):
#         if request.method == 'POST':

#             username = request.POST.get('username', None)
#             password = request.POST.get('password', None)

#             return sign_up_view, HttpResponse("환영합니다!")    

def sign_up_view(request):
    if request.method == 'POST':

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        return HttpResponse("환영합니다!")    