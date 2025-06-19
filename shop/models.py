from django.db import models
from datetime import datetime
from membership.models import Member, Federation

class DiscountType(models.TextChoices):
    SUBTRACT = "S","Réduction directe"
    PERCENTAGE = "P","Pourcentage"
    FINAL_PRICE = "F","Prix final"

class ProductGroup(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=150,null=True)

class Product(models.Model):
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=150,null=True)
    groups = models.ManyToManyField(ProductGroup,related_name="products")

class Store(models.Model):
    # A Store belongs to a federation
    name = models.CharField(max_length=100,null=True)
    description = models.TextField(max_length=150,null=True)
    federation = models.OneToOneField(Federation,null=True,on_delete=models.RESTRICT)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ["federation","name"],name = "unique_storeNamePerFederation")
        ]

class ProductInStore(models.Model):
    product = models.ForeignKey(Product,null=True,on_delete=models.RESTRICT)
    store = models.ForeignKey(Store,null=True,related_name="productsInStore",on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=0)
    current_price = models.FloatField(null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ["product","store"],name = "unique_productInStore")
        ]

    def __str__(self):
        return str(self.quantity) +" items of "+self.product.name + " are present in " + self.quantity

class Discount(models.Model):
    #   A discount concerns a product in store.
    productInStore = models.ForeignKey(ProductInStore,null=True,related_name="discounts",on_delete=models.RESTRICT)
    creation_date = models.DateTimeField(null=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    type = models.CharField(max_length=20,choices=DiscountType.choices,default=DiscountType.PERCENTAGE)
    amount = models.FloatField()

class StorageChange(models.Model):
    productInStore = models.ForeignKey(ProductInStore,null=True,on_delete=models.RESTRICT)
    creation_date = models.DateTimeField(default = datetime.now)
    due_date = models.DateTimeField(null=True)
    done_date = models.DateTimeField(null=True)
    added_quantity = models.IntegerField(default=1)
    comment = models.TextField(max_length=100,null=True)
    def __str__(self):
        return "On "+ self.date +", "+ str(self.added_quantity) +" items of "+self.productInStore.product.name + " were added in " + self.productInStore.store.name

class Cart(models.Model):
    creation_date = models.DateTimeField(default=datetime.now)
    order_date = models.DateTimeField(null=True)
    payment_date = models.DateTimeField(null=True)
    delivery_date = models.DateTimeField(null=True)
    cancelling_date = models.DateTimeField(null=True)
    orderer = models.ForeignKey(Member,null=True,on_delete=models.RESTRICT)
    def __str__(self):
        return self.orderer.first_name + " " + self.orderer.name + " " + self.creation_date

class OrderLine(models.Model):
    cart = models.ForeignKey(Cart,null=True,on_delete=models.RESTRICT)
    productInStore = models.ForeignKey(ProductInStore,null=True,on_delete=models.RESTRICT)
    quantity = models.FloatField(default=1)
    used_price = models.FloatField(null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ["productInStore","cart"],name = "unique_orderLine")
        ]
    
    def __str__(self):
        return self.productInStore.product.name + " " + self.productInStore.current_price + " " + self.used_price

class PriceChange(models.Model):
    productInStore = models.ForeignKey(ProductInStore,null=True,on_delete=models.RESTRICT)
    creation_date = models.DateTimeField(default = datetime.now)
    change_date = models.DateTimeField(null=True)
    new_price = models.FloatField(null=True)
    author = models.ForeignKey(Member,null=True,on_delete=models.RESTRICT)
    def __str__(self):
        return self.productInStore.product.name + " " + self.productInStore.current_price + " " + self.productInStore.current_price
