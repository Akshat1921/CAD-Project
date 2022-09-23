from rest_framework import serializers
from .models import Book
from .models import StockFile
 
#This is for image
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'cover']
 

#This is for File
class StockFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StockFile
        fields = ['name','price','volume','info']