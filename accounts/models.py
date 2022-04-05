from stats.models import PublicStatisticsModel, PrivateStatisticsModel
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    GENDERS = (
        ('m', 'Man'),
        ('w', 'Woman')
    )
    first_name = models.CharField(max_length=30)
    last_name =  models.CharField(max_length=30)
    email = models.EmailField()
    gender = models.CharField(max_length=1, choices=GENDERS, default=' ')
    info = models.CharField(max_length=700, blank=True)
    birth_date = models.DateField(default='2000-01-01')
    public_stat = models.OneToOneField(PublicStatisticsModel, on_delete=models.CASCADE, null=True)
    private_stat = models.OneToOneField(PrivateStatisticsModel, on_delete=models.CASCADE, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
