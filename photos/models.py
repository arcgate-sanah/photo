from django.db import models

class Photos(models.Model):

    def __str__(self):
        return self.item_name
    
    photos_category = models.ImageField()
   