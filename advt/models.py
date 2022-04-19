from django.db import models
from django.contrib.auth import get_user_model
'''
import datetime

date = datetime.datetime.strptime('2020-12-12', "%Y-%m-%d")
res = date + datetime.timedelta(days=1)

print(res.date()
'''
User = get_user_model()
#пост для поиска напариников для игры
class PostModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    pub_date = models.DateField(auto_now_add=True)
    city = models.CharField(max_length=2)#заменить на поле города!!
    del_date = models.DateField(blank=True)
