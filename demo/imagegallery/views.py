from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import HttpResponse
from .serializer import BookSerializer
from .serializer import StockFileSerializer
from .models import Book
from .models import StockFile
 
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import FormParser, MultiPartParser

#this view is for Image 
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
 
    def post(self, request, *args, **kwargs):
        cover = request.data['cover']
        title = request.data['title']
        Book.objects.create(title=title, cover=cover)
        return HttpResponse({'message': 'created'}, status=200)
 
    def get(self,request):
        list = Book.objects.all()
        serializ = BookSerializer(list,many=True)
        return HttpResponse(serializ.data)
    
     
#this view is for File and data
class FileUploadViewSet(viewsets.ModelViewSet):
    queryset = StockFile.objects.all()
    serializer_class = StockFileSerializer
 
    def get(self,request):
        list = StockFile.objects.all()
        serializ = StockFileSerializer(list,many=True)
        return HttpResponse(serializ.data)
 
    def post(self, request, *args, **kwargs):
        name = request.data['name']
        price = request.data['price']
        volume = request.data['volume']
        info = request.data['info']
        StockFile.objects.create(name=name,price=price,volume=volume,info=info)
        return HttpResponse({'message': 'Book created'}, status=200)