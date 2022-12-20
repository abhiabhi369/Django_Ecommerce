from rest_framework.views import APIView
from rest_framework.response import Response

from flip_app.models import Users, Products, Category
from flip_app.serializer import CategorySerializer,ProductViewSerializer
from flip_app.Permissions import UserAuthentication,UserAuthenticationOrReadOnly



class ProductView(APIView):
    permission_classes = [UserAuthenticationOrReadOnly]
    def get(self,request):
        all_products = Products.objects.all()
        print('all_products',all_products)
        print('before serializer')
        serializer = ProductViewSerializer(all_products,many=True)
        print('after serializer')
        print('serializer',serializer)
        return Response(serializer.data)

    def post(self,request):
        print('data',request.data)
        cat = request.data.pop('category')
        serializer = ProductViewSerializer(data=request.data)
        if serializer.is_valid():
            inst = serializer.save()
            all_cat_list = list(Category.objects.values_list('category', flat=True))
            for category in cat:
                if category in all_cat_list:
                    cat_inst = Category.objects.filter(category=category)
                    inst.category.set(cat_inst)
                else:
                    cat_inst = Category.objects.create(category=category)
                    inst.category.add(cat_inst)
        else:
            print('errors',serializer.errors)
        return Response({"Message":"ok"})


