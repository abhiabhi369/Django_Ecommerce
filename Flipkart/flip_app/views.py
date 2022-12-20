from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.permissions import IsAuthenticated

from .serializer import *
from .forms.register import RegisterForm,LoginForm
from flip_app.Permissions import UserAuthentication

import random
import string

class Home(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Home.html'
    def get(self,request):
        return Response({'message':'Welcome to Flipkart'})

class RegistrationByPostman(APIView):
    def get(self,request):
        form = RegisterForm()
        print(form)
        return Response({'message':'This is registaration page'})

    def post(self,request):
        print(request.data)
        if request.data['password'] != request.data['password1']:
            return Response({"password error":"passwords does not match"})
        serializer = RegisterSerializer(data=request.data)
        print('serializer',serializer)
        if serializer.is_valid():
            print('is valid')
            serializer.save()
        else:
            print('serializer.errors',serializer.errors)
            return Response(serializer.errors)
        # print('serializer',serializer)
        return Response(request.data)

class RegisterationByForm(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'register.html'

    def get(self,request):
        form = RegisterForm
        return Response({'message':'Register Here','form':form,'show':'show'})
    def post(self,request):
        print('request',request.POST)
        form = RegisterForm(request.POST)
        # print('form',form)
        if form.is_valid():
            print('in valid')
            form.save()
            return Response({'message': 'Registered Successfully..!!'})
        else:
            print('in else')
            print(type(form.errors))
            return Response(form.errors)
        # return HttpResponseRedirect('/app/registe')

class LoginPostman(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'Login.html'
    def token(self):
        letters = string.ascii_letters+string.digits
        return ''.join(random.sample(letters,30))
    def get(self,request):
        form = LoginForm
        return Response({'message':'Please login here','form':form,'nologin':True})

    def post(self,request):
        data = request.POST
        print('data',data)
        all_users = list(Users.objects.all().values_list('email',flat=True))
        print('all_users',all_users)
        if data['Username'] in all_users:
            password = Users.objects.all().filter(email=data['Username']).values_list('password',flat=True).first()
            if password == data['Password']:
                print('password ok')
                token = self.token()
                Users.objects.filter(email=data['Username']).update(token=token)
                response = Response({'message': 'Logedin Successfuly', 'token': token,'login':True})
                response.set_cookie('token_value', token, max_age=None, httponly=True)
                # return Response({'message':'Logedin Successfuly','login':True})
                return response
            else:
                # return Response({'message':'Password incorrect','login':True})
                return HttpResponseRedirect('/app/login')

def set_cookie(token,response):
    response = response.set_cookie('token_value', token, max_age=None,httponly=True)
    return response

class Login(APIView):
    def token(self):
        letters = string.ascii_letters+string.digits
        return ''.join(random.sample(letters,30))
    def post(self,request):
        data = request.data
        print('data', data)
        all_users = list(Users.objects.all().values_list('email', flat=True))
        if data['Username'] in all_users:
            print('username ok')
            password = Users.objects.all().filter(email=data['Username']).values_list('password', flat=True).first()
            if password == data['Password']:
                print('password ok')
                token = self.token()
                Users.objects.filter(email=data['Username']).update(token=token)
                response = Response({'message': 'Logedin Successfuly','token':token})
                response.set_cookie('token_value',token,max_age=None,httponly=True)
                # response = set_cookie(token,response)
                print('response',response)
                return response
            else:
                return HttpResponseRedirect('/app/login')
        else:
            return Response({"message":"Not registered yet..."})


class Restrict(APIView):
    permission_classes = [UserAuthentication]
    def get(self,request):
        print('request',request)
        print('request.META',request.META.get('HTTP_AUTHORIZATION'))
        return Response({"message":"you are unrestricted now...!!"})

class UserLogout(APIView):
    permission_classes = [UserAuthentication]
    def get(self,request):
        # token = request.META.get('HTTP_AUTHORIZATION')
        token = request.COOKIES.get('token_value')
        print('token',token)
        tk = Users.objects.filter(token=token).update(token='')
        print('tk',tk)
        response = Response({"message":"Logout successfull"})
        set_cookie('',response=response)
        # tk.token = ''
        # tk.save()
        return response

class Cookie(APIView):
    def get(self,request):
        print('request',request)
        response = Response()
        response.set_cookie('abhi_cookie','this is the value of the cookie for example token',max_age=None)
        return response
    def post(self,request):
        print('request',request.META)
        print('request.COOKIES',request.COOKIES.get('abhi_cookie'))
        return Response({"message":request.COOKIES})




