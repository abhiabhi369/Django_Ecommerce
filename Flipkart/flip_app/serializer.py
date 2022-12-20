from rest_framework import serializers
from .models import Users,Products,Category,Order

class RegisterSerializer(serializers.ModelSerializer):
    # password1 = serializers.CharField(style={"input_type": "password"}, write_only=False)
    class Meta:
        model = Users
        fields = '__all__'

    # def save(self, **kwargs):
    #     password = self.validated_data['password']
    #     password1 = self.validated_data['password1']
    #
    #     if password != password1:
    #         raise serializers.ValidationError({"error":"password does not match..!!"})
    #     account = Users(password=password,email=self.validated_data['email'])
    #
    #     return account



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductViewSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True,many=True)
    class Meta:
        model = Products
        fields = '__all__'

    # def create(self, validated_data):
    #     print('validated_data',validated_data)
        # category_data = validated_data.pop('category')
        # print('category_data',category_data)
        # instance = super(ProductViewSerializer,self).create(validated_data)
        # if category_data['category'] in list(Category.objects.values_list('category',flat=True)):
        #     category = category_data['category']
        # else:
        #     category = Category.objects.create(**category_data)
        # products = Products.objects.create(**validated_data)
        # req_cat = Category.objects.filter(category=category)
        # print('req_cat',req_cat)
        # products.category.set(req_cat)
        # return products

class OrderSerializer(serializers.ModelSerializer):
    # user = RegisterSerializer(source='Users.first')
    class Meta:
        model = Order
        fields = '__all__'
    def to_representation(self, instance):
        print('instance',instance)
        self.fields['user'] = RegisterSerializer(read_only=True)
        self.fields['product'] = ProductViewSerializer(read_only=True)
        return super(OrderSerializer,self).to_representation(instance)



