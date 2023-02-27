from django.shortcuts import render

from json import JSONDecodeError
from django.http import JsonResponse
from .serializers import ContactSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response

# The ContactAPIView class inherits from views.APIView, which provides a generic class-based view for handling HTTP requests.
class ContactAPIView(views.APIView):
    """
    A simple APIView for creating contact entires.
    """

    # 'serializer_class': a class attribute that specifies the serializer class to use for the view.
    serializer_class = ContactSerializer

    # 'get_serializer_context()': a method that returns a dictionary of context information to be passed to the serializer.
    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    # 'get_serializer()': a method that returns an instance of the serializer class with the appropriate context.
    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    # 'post()': a method that handles HTTP POST requests to the view.
    def post(self, request):
        try:
            # It parses the request data using JSONParser()
            data = JSONParser().parse(request)
            # creates a new instance of the serializer with the parsed data
            serializer = ContactSerializer(data=data)

            # and then checks if the serializer is valid using serializer.is_valid(). If the serializer is valid, it saves the data and returns a Response object with the serialized data.
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
            # If the serializer is not valid, it returns a Response object with the serializer errors and a status code of HTTP_400_BAD_REQUEST.
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # 'JSONDecodeError': an exception that is raised if there is an error in decoding the JSON data.
        except JSONDecodeError:
            return JsonResponse({"result": "error","message": "Json decoding error"}, status= 400)