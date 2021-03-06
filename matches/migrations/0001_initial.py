# Generated by Django 3.2.9 on 2022-04-05 10:36

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MatchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.IntegerField(default=0)),
                ('score2', models.IntegerField(default=0)),
                ('set1p1', models.IntegerField(default=0)),
                ('set1p2', models.IntegerField(default=0)),
                ('set2p1', models.IntegerField(default=0)),
                ('set2p2', models.IntegerField(default=0)),
                ('set3p1', models.IntegerField(default=0)),
                ('set3p2', models.IntegerField(default=0)),
                ('set4p1', models.IntegerField(default=0)),
                ('set4p2', models.IntegerField(default=0)),
                ('set5p1', models.IntegerField(default=0)),
                ('set5p2', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('slug', models.CharField(max_length=40)),
                ('video', models.FileField(blank=True, upload_to='videos/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mov', 'mp4', 'wmv', 'avi'])])),
                ('is_public', models.BooleanField(default=False)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('p1', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p1', to=settings.AUTH_USER_MODEL)),
                ('p2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='p2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
