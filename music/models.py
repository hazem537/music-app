from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.



class Song(models.Model):
    name = models.CharField( max_length=50 )
    slug = models.SlugField( blank=True)
    singer = models.CharField( max_length=50)
    tags = models.CharField( max_length=50)
    image= models.ImageField( upload_to="images") 
    audio = models.FileField( upload_to="audios", max_length=100)
    user = models.ForeignKey(User,related_name="songs", on_delete=models.CASCADE)
    public = models.BooleanField(default=True)

    class Meta:
         unique_together= ( "slug","user")
    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
            super().save(*args, **kwargs)