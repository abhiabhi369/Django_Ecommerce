from django.db import models

# Create your models here.
class Users(models.Model):
    Gender_Choice = (('M','Male'),
                     ('F','Female')
                     )
    first = models.CharField(max_length=30,null=False)
    last = models.CharField(max_length=30,null=False)
    Gender = models.CharField(choices=Gender_Choice,max_length=1)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50,null=False,unique=True,error_messages={'unique':'This email already exist'})
    password = models.CharField(max_length=10,null=False)
    # password1 = models.CharField(max_length=10,null=False)
    token = models.CharField(max_length=35,null=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

class Products(models.Model):
    name = models.CharField(max_length=50,null=False)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    category = models.ManyToManyField(Category,related_name='pcategory')
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(Users,related_name='users',on_delete=models.CASCADE)
    product = models.ForeignKey(Products,related_name='products',on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=7,decimal_places=2)

    def __str__(self):
        return str(self.product)


