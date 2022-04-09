from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date_pub = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=15)
    delete_date = models.DateField(blank=True)
