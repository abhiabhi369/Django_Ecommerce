from rest_framework.views import APIView
from rest_framework.response import Response

from flip_app.models import Users,Products,Category,Order
from flip_app.serializer import RegisterSerializer,OrderSerializer,ProductViewSerializer
from flip_app.Permissions import UserAuthentication, UserAuthenticationOrReadOnly

class OrderView(APIView):
    permission_classes = [UserAuthentication]
    def get(self,request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders,many=True)
        print('serializer data',serializer.data)
        return Response(serializer.data)

    def post(self,request):
        print('request',request.data)
        print(request.META.get('HTTP_AUTHORIZATION'))
        token = request.META.get('HTTP_AUTHORIZATION')
        user = list(Users.objects.filter(token=token).values_list('pk',flat=True))
        print('user',user)
        product = Products.objects.filter(pk=request.data['product']).values()
        print('product',product)
        for i in product:
            print('for',i['price'])
            price = i['price']
        data = {"user":user[0],"product":request.data['product'],"total_amount":price}
        serializer = OrderSerializer(data=data)
        print('serializer',serializer)
        if serializer.is_valid():
            serializer.save()
        else:
            print('errors',serializer.errors)

        return Response({"message":"Posted"})

class OrderList(APIView):
    permission_classes = [UserAuthentication]
    def get(self,request):
        token = request.META.get('HTTP_AUTHORIZATION')
        user = list(Users.objects.filter(token=token).values_list('pk', flat=True))
        orders = Order.objects.filter(user=user[0])
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
