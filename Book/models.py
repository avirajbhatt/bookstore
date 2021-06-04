from django.db import models



class Book(models.Model):
    bookname = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)
    image = models.ImageField(upload_to="media")
    email = models.EmailField(blank=False, default='')

    @staticmethod
    def get_all_books():
        return Book.objects.all()
