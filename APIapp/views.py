from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
an_apiview = [
            'uses HTTP methods as function (get, post, put, patch, delete)',
            'Is similar to a traditional django view',
            'gives you the most control over your application logic',
            'is mapped manually to URLs',
        ]

def home(request):
    global an_apiview
    context = {
        'an_apiview':an_apiview
    }
    return render(request,'home.html',context)

def login(request):
    return render(request,'login.html')

class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        '''Returns a list of APIView Items'''
        global an_apiview
        return Response({'message':'Hello..!','an_apiview':an_apiview})