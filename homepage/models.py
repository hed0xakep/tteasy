from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.shortcuts import reverse
from django.db import models
from time import time

# Create your models here.



def generate_slug(title):
    return slugify(title, allow_unicode=True) +'-' + str(int(time()))

class Homepost(models.Model): #post model on main page
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=30, unique=True)
    body = models.TextField(db_index=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='homeposts/', validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png'])], blank=True)


    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug': self.slug})


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = generate_slug(self.title)
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.title} - {self.slug}'
