from rest_framework import permissions
from flip_app.models import Users

class UserAuthentication(permissions.BasePermission):
    def has_permission(self, request, view):
        if  request.META.get('HTTP_AUTHORIZATION') is not None:
            print('token',request.META.get('HTTP_AUTHORIZATION'))
        else:
            print('in else')
            if request.COOKIES.get('token_value') is not None:
                token = request.COOKIES.get('token_value')
                print('token',token)
            else:
                print('in else')
        print('in authentication')
        # print('token',request.COOKIES.get('token_value'))
        if token is not '' and token in list(Users.objects.values_list('token',flat=True)):
            print('token found')
            return True
        else:
            return False

class UserAuthenticationOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            token = request.META.get('HTTP_AUTHORIZATION')
        except:
            if request.COOKIES.get('token_value') is not None:
                token = request.COOKIES.get('token_value')
                print('token',token)
            print('token',request.COOKIES.get('token_value'))
        print('in authentication')
        print('token',request.COOKIES.get('token_value'))
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            user = Users.objects.filter(token=token).values()
            for i in user:
                if i['is_admin'] == True:
                    return True
                else:
                    return False
