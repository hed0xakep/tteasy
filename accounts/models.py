from stats.models import PublicStatisticsModel, PrivateStatisticsModel
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager
from django.db import models



class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Man'),
        ('w', 'Woman')
    )
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDERS, default='m')
    info = models.CharField(max_length=700, blank=True)
    public_stat = models.OneToOneField(PublicStatisticsModel, on_delete=models.CASCADE, null=True, related_name='user')
    private_stat = models.OneToOneField(PrivateStatisticsModel, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    objects = UserManager()
