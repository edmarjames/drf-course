# import OrderedDict to use 'res'
from collections import OrderedDict

# import models
from .models import Item , Order

# import dependencies from rest_framework
from rest_framework_json_api import serializers
from rest_framework import status
# this is used for raising API exceptions
from rest_framework.exceptions import APIException



# custom exception with status code of 400 and default message
class NotEnoughStockException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'There is not enough stock'
    default_code = 'invalid'




class ItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        # declare the model
        model = Item
        # fields that should be serialized/deserialized when dealing with Item objects, namely title, stock, and price.
        fields = (
            'title',
            'stock',
            'price',
        )




class OrderSerializer(serializers.ModelSerializer):

    # This field is used to serialize and deserialize the related Item object for an order using its primary key.

    # The queryset parameter specifies the set of items that can be selected for the Order object, which in this case is all items in the database.

    # The many parameter is set to False, indicating that only one Item object can be selected for the Order.
    item = serializers.PrimaryKeyRelatedField(queryset = Item.objects.all(), many=False)
    
    class Meta:
        # declare the model
        model = Order
        # fields that should be serialized/deserialized when dealing with Order objects, namely item and quantity
        fields = (
            'item',
            'quantity',
        )

    # This code defines a validate method for the OrderSerializer class. When is_valid() method of the serializer is called, the validate() method is called to validate the input data.
    def validate(self, res: OrderedDict):
        '''
        Used to validate Item stock levels
        '''

        # The "get" method of OrderedDict is used to retrieve the value of the "item" and "quantity" keys that is being validated in the serializer.
        item = res.get("item")
        quantity = res.get("quantity")

        # validates the item's stock level by checking if the requested quantity exceeds the available stock. If the stock is insufficient, it raises a custom exception
        if not item.check_stock(quantity):
            raise NotEnoughStockException
        return res