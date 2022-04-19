from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from user.models import ProfileModel
from django.contrib.auth import get_user_model

User = get_user_model()

class MatchModel(models.Model):
    p1 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='p1')#models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    p2 = models.ForeignKey(User, on_delete=models.PROTECT, related_name='p2')
    score1 = models.IntegerField(default=0)#first player's score
    score2 = models.IntegerField(default=0)
    set1p1 = models.IntegerField(default=0)
    set1p2 = models.IntegerField(default=0)
    set2p1 = models.IntegerField(default=0)
    set2p2 = models.IntegerField(default=0)
    set3p1 = models.IntegerField(default=0)
    set3p2 = models.IntegerField(default=0)
    set4p1 = models.IntegerField(default=0)
    set4p2 = models.IntegerField(default=0)
    set5p1 = models.IntegerField(default=0)
    set5p2 = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=40)
    video = models.FileField(upload_to='videos/%Y/%m/%d/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['mov', 'mp4', 'wmv', 'avi'])])
    is_public = models.BooleanField(default=False)
    is_confirmed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detail_match', kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.p1}-{self.p2}({self.score1}-{self.score2})_{str(self.date)[:10]}'
