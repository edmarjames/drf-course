from django.db import models

# import User model
from django.contrib.auth.models import User

# import the Model from utils folder
from utils.model_abstracts import Model

# import dependencies for abstract model classes
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleSlugDescriptionModel
)


# create a Item model and inherit abstract model classes
# 'TimeStampedModel' - adds fields for creation and modification timestamps to the model.
# 'ActivatorModel' - adds fields for activation status to the model.
# 'TitleDescriptionModel' - adds fields for title and description to the model.
# 'Model' - an abstract model defined in a separate module that adds some utility methods for querying the model
class Item(
    TimeStampedModel,
    ActivatorModel ,
    TitleSlugDescriptionModel,
    Model):

    """
    ecommerce.Item
    Stores a single item entry for our shop
    """

    class Meta:
        # verbose_name specifies the human-readable name for a single object of the model. In this case, it sets the name to 'Item'.
        verbose_name = 'Item'
        # verbose_name_plural specifies the human-readable name for multiple objects of the model. In this case, it sets the name to 'Items'.
        verbose_name_plural = 'Items'
        # ordering specifies the default ordering of the model instances when queried from the database. In this case, it orders by the id field.
        ordering = ["id"]

    def __str__(self):
        return self.title
    
    # adds stock and price fields
    stock = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    def amount(self):
        #converts price from pence to pounds
        amount = float(self.price / 100)
        return amount

    def manage_stock(self, qty):
        #used to reduce Item stock
        new_stock = self.stock - int(qty)
        self.stock = new_stock
        self.save()


    def check_stock(self, qty):
        #used to check if order quantity exceeds stock levels
        if int(qty) > self.stock:
            return False
        return True

    def place_order(self, user, qty):
        #used to place an order
        if self.check_stock(qty):
            order = Order.objects.create(
                item = self, 
                quantity = qty, 
                user= user)
            self.manage_stock(qty)
            return order
        else:
            return None




class Order(
    TimeStampedModel,
    ActivatorModel ,
    Model):
    """
    ecommerce.Order
    Stores a single order entry, related to :model:`ecommerce.Item` and
    :model:`auth.User`.
    """
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        ordering = ["id"]
    
    # a foreign key to the User model
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    #  a foreign key to the Item model
    item = models.ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    # integer field to store the quantity of the ordered item
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.item.title}'