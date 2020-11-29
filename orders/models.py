from django.db import models
from django.contrib.auth.models import User


class Referrer(models.Model):
    user        = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    name        = models.CharField(max_length=50)
    surname     = models.CharField(max_length=50)
    email       = models.EmailField()
    phone       = models.CharField(max_length=15)
    occupation  = models.CharField(max_length=50)
    institution = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username + self.occupation


class Recipient(models.Model):
    full_name   = models.CharField(max_length=50)
    email       = models.EmailField(blank=True)
    phone       = models.CharField(max_length=15)
    refereed_by  = models.ForeignKey(Referrer, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Delivery_Address(models.Model):
    recipient           = models.ForeignKey(Recipient, null=True, on_delete=models.SET_NULL)
    address_line        = models.CharField(max_length=50)
    post_code           = models.CharField(max_length=10)
    directions          = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.address_line


class Product_Tag(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Product(models.Model):

    CATEGORY = (
        ('F&VBox', 'F&VBox'),
        ('Invoice', 'Invoice'),
        ('Essential', 'Essential'),
        ('T&M', 'T&M'),
        ('Project', 'Project'),
        ('Other', 'Other'),
    )

    name                = models.CharField(max_length=50)
    price               = models.FloatField()
    category            = models.CharField(max_length=50, choices=CATEGORY)
    product_tag         = models.ManyToManyField(Product_Tag)
    description         = models.CharField(max_length=200, blank=True)
    day_created         = models.DateTimeField(auto_now_add=True)
    active              = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
        ('SO', 'Standing Order'),
    )


    DELIVERY_DAY = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('pickup', 'pickup'),
    )

    RUN = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    referrer            = models.ForeignKey(Referrer, null=True, on_delete=models.SET_NULL)
    recipient           = models.ForeignKey(Recipient, null=True, on_delete=models.SET_NULL)   
    product             = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    delivery_address    = models.ForeignKey(Delivery_Address, related_name='delivery_address', null=True, on_delete=models.SET_NULL)
    comments            = models.TextField(max_length=500, blank=True)
    date_created        = models.DateTimeField(auto_now_add=True)
    status              = models.CharField(max_length=100, blank=True, choices=STATUS)
    delivery_day        = models.CharField(max_length=100, blank=True, choices=DELIVERY_DAY)
    run                 = models.CharField(max_length=100, blank=True, choices=RUN)

    def __str__(self):
        return self.recipient.full_name + self.product.name



