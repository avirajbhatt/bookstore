from django.contrib import admin
from .models import Book


class AdminBook(admin.ModelAdmin):
    list_display = ['bookname', 'description']


admin.site.register(Book, AdminBook)
admin.site.site_header = 'Book Store'
