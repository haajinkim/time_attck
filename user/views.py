from operator import attrgetter
from django.shortcuts import render, redirect

# Create your views here.

def sign_up_view(request):
   
    if request.method == 'POST':
            username = request.POST.get('username', None)
            password = request.POST.get('password', None)

            return render(request)

# class User:

#     def __init__(self):

#         self.email = ''  
#         self.password = ''  
#         self.attribute = '' 



# user = User()
# user.email = '첫 게시글'
# user.password = 'sparta'
# user.attribute = '나의 첫 python Class 게시글은 sparta에서'