from django.db import models

# Create your models here.
class PublicStatisticsModel(models.Model):
    wins = models.PositiveSmallIntegerField(default=0)
    loses = models.PositiveSmallIntegerField(default=0)
    dry_wins = models.PositiveSmallIntegerField(default=0)#победы всухую
    dry_loses = models.PositiveSmallIntegerField(default=0)#сухие проигрыши
    s1_win = models.PositiveSmallIntegerField(default=0)
    s1_l = models.PositiveSmallIntegerField(default=0)
    s2_win = models.PositiveSmallIntegerField(default=0)
    s2_l = models.PositiveSmallIntegerField(default=0)
    s3_win = models.PositiveSmallIntegerField(default=0)
    s3_l = models.PositiveSmallIntegerField(default=0)
    s4_win = models.PositiveSmallIntegerField(default=0)
    s4_l = models.PositiveSmallIntegerField(default=0)
    s5_win = models.PositiveSmallIntegerField(default=0)
    s5_l = models.PositiveSmallIntegerField(default=0)

class PrivateStatisticsModel(models.Model):
    wins = models.PositiveSmallIntegerField(default=0)
    loses = models.PositiveSmallIntegerField(default=0)
    dry_wins = models.PositiveSmallIntegerField(default=0)
    dry_loses = models.PositiveSmallIntegerField(default=0)
    s1_win = models.PositiveSmallIntegerField(default=0)
    s1_l = models.PositiveSmallIntegerField(default=0)
    s2_win = models.PositiveSmallIntegerField(default=0)
    s2_l = models.PositiveSmallIntegerField(default=0)
    s3_win = models.PositiveSmallIntegerField(default=0)
    s3_l = models.PositiveSmallIntegerField(default=0)
    s4_win = models.PositiveSmallIntegerField(default=0)
    s4_l = models.PositiveSmallIntegerField(default=0)
    s5_win = models.PositiveSmallIntegerField(default=0)
    s5_l = models.PositiveSmallIntegerField(default=0)
