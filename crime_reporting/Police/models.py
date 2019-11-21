from django.db import models
from PIL import Image

# Create your models here.
class Missing(models.Model):
    name = models.CharField(max_length=20)
    mobile = models.IntegerField(default=0)
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=20)
    image = models.ImageField(upload_to='missing_people', blank=True)
    details = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class wanted(models.Model):
    uname = models.CharField(max_length=20)
    height = models.IntegerField(default=0)
    color = models.CharField(max_length=20)
    crime_type = models.CharField(max_length=20)
    crime_area = models.CharField(max_length=20)
    crime_spot = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='wanted_people', blank=True,null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.uname

    def save(self):
        super().save()

        img = Image.open(self.photo.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.photo.path)
