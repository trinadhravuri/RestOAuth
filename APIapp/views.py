from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from APIapp import serializers

# Create your views here.
an_apiview = [
            'uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]

def home(request):
    global an_apiview
    
    serializer_class = serializers.HelloSerializer
    serializer = serializer_class(data = request.body)

    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        message = f"Hello ..! {name}"
        serializer.save()
    name = serializer.validated_data.get('name')
    message = f"Hello ..! {name}"
    context = {
        'an_apiview':an_apiview,
        'message':message,
        'serializer':serializer,
    }

    return render(request,'home.html',context)

def login(request):
    return render(request,'login.html')

class HelloApiView(APIView):
    '''Test API View'''

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        '''Returns a list of APIView Items'''
        global an_apiview
        return Response({'message':'Hello..!','an_apiview':an_apiview})
    
    def post(self, request):
        """Create a hello message with our name in serializer"""
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hello ..! {name}"
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({"method":'PUT'})
    def patch(self, request, pk = None):
        """Handle Update a field from patch"""
        return Response({'method':'PATCH'})
    def delete(self, request,pk = None):
        """Perform Delete operation on object"""
        return Response({"method":"DELETE"})