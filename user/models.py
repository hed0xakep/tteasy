from stats.models import PublicStatisticsModel, PrivateStatisticsModel
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    objects = UserManager()

class ProfileModel(models.Model):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile', null=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name =  models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default='m')
    info = models.CharField(max_length=700, blank=True)
    public_stat = models.OneToOneField(PublicStatisticsModel, on_delete=models.CASCADE, null=True, related_name='profile')
    private_stat = models.OneToOneField(PrivateStatisticsModel, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            pub_stat = PublicStatisticsModel.objects.create()
            private_stat = PrivateStatisticsModel.objects.create()
            self.private_stat = private_stat
            self.public_stat = pub_stat
        super().save(*args, **kwargs)
