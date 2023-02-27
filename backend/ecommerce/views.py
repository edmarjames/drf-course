# import JSONDecodeError and JsonResponse
from json import JSONDecodeError
from django.http import JsonResponse

# import the serializers
from .serializers import ItemSerializer, OrderSerializer
# import the models
from .models import Item , Order

# import JSONParser, isAuthenticated, viewsets, status, Response and mixins from rest_framework
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin,UpdateModelMixin,RetrieveModelMixin


# ItemViewSet provides two endpoints for listing and retrieving items. The ListMixin and RetrieveModelMixin are used for this purpose.
class ItemViewSet(
        ListModelMixin,
        RetrieveModelMixin, 
        viewsets.GenericViewSet
        ):
    """
    A simple ViewSet for listing or retrieving items.
    """

    # allow only authenticated users to access the endpoints.
    permission_classes = (IsAuthenticated,)

    #  to return all Item instances.
    queryset = Item.objects.all()

    # specifies ItemSerializer as the serializer class
    serializer_class = ItemSerializer



# OrderViewSet provides three endpoints for listing, retrieving, and creating orders. The ListMixin, RetrieveModelMixin, and UpdateModelMixin are used to provide these functionalities.
class OrderViewSet(
        ListModelMixin,
        RetrieveModelMixin,
        UpdateModelMixin, 
        viewsets.GenericViewSet
        ):
    """
    A simple ViewSet for listing, retrieving and creating orders.
    """

    # allow only authenticated users to access the endpoints.
    permission_classes = (IsAuthenticated,)

    # specifies OrderSerializer as the serializer class 
    serializer_class = OrderSerializer

    # The get_queryset() method is overridden to return all orders for the authenticated user.
    def get_queryset(self):
        """
        This view should return a list of all the orders
        for the currently authenticated user.
        """
        user = self.request.user
        return Order.objects.filter(user = user)

    # The create() method is also overridden to handle the creation of new orders
    def create(self, request):
        try:
            # It first parses the request data
            data = JSONParser().parse(request)
            # uses the OrderSerializer to validate the data.
            serializer = OrderSerializer(data=data)

            # If the data is valid
            if serializer.is_valid(raise_exception=True):
                # it gets the Item instance based on the item primary key provided in the request data
                item = Item.objects.get(pk = data["item"])
                # places the order for the specified quantity
                order = item.place_order(request.user, data["quantity"])
                # The OrderSerializer is then used to serialize the newly created Order instance and returns it in the response.
                return Response(OrderSerializer(order).data)
            
            # If the data is not valid, it returns the validation errors in the response.
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        # In case of a JSON decoding error, the create() method returns a JSON response with an error message and status code 400.
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)