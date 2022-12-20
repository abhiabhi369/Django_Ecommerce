from django.urls import path
from .views import Home,RegistrationByPostman,RegisterationByForm,Login,LoginPostman,Restrict,UserLogout,Cookie
from flip_app.products import ProductView
from flip_app.Order import OrderView,OrderList

from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView

urlpatterns = [
    path('home/',Home.as_view(),name='Home'),
    path('register/',RegisterationByForm.as_view(),name='Register'),
    path('registe/',RegistrationByPostman.as_view(),name='register'),
    path('login/',LoginPostman.as_view(),name='Login'),
    path('loginpostman/',Login.as_view(),name='Login-Token'),
    path('restrict/',Restrict.as_view(),name='Restrict'),
    path('ulogout/',UserLogout.as_view(),name='Logout'),
    path('products/',ProductView.as_view(),name='Product'),
    path('order/',OrderView.as_view(),name='Order'),
    path('orderlist/',OrderList.as_view(),name='Order-List'),
    path('cookie/',Cookie.as_view(),name='Cookie'),

    path('api/token/',TokenObtainPairView.as_view(),name='Token-Obtain'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='Token-Refresh')
]