from django.db import models

# Create your models here.

class Category(models.Model):
    cat_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.cat_name

class Book(models.Model):
    category = models.ForeignKey(Category , on_delete=models.CASCADE) 
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name
    
 