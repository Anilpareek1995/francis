from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from django.utils import timezone

# Create your models here.
class Complaint(models.Model):
    username = models.CharField(max_length=20)
    mobile = models.IntegerField()
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=20)
    complaint_title = models.CharField(max_length=30)
    complaint_details = models.CharField(max_length=100)

    
    def __str__(self):
        return self.username

class plogin(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.username} Police Station'

class feedback(models.Model):
    username = models.CharField(max_length=20)
    mobile = models.IntegerField()
    address = models.CharField(max_length=80)
    city = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    feedback = models.CharField(max_length=100)

    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title