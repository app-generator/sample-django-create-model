from django.db import models

class Book(models.Model): 
    title            = models.CharField(max_length=100) 
    author           = models.CharField(max_length=100)
    publication_date = models.DateField() 

    # Implements the string representation
    def __str__(self):
        return self.title 
 