from django.contrib import admin
from .models import Book
from .models import StockFile
 
admin.site.register(Book)
admin.site.register(StockFile)