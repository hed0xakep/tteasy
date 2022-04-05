# Generated by Django 3.2.9 on 2022-04-05 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateStatisticsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('loses', models.PositiveSmallIntegerField(default=0)),
                ('dry_wins', models.PositiveSmallIntegerField(default=0)),
                ('dry_loses', models.PositiveSmallIntegerField(default=0)),
                ('s1_win', models.PositiveSmallIntegerField(default=0)),
                ('s1_l', models.PositiveSmallIntegerField(default=0)),
                ('s2_win', models.PositiveSmallIntegerField(default=0)),
                ('s2_l', models.PositiveSmallIntegerField(default=0)),
                ('s3_win', models.PositiveSmallIntegerField(default=0)),
                ('s3_l', models.PositiveSmallIntegerField(default=0)),
                ('s4_win', models.PositiveSmallIntegerField(default=0)),
                ('s4_l', models.PositiveSmallIntegerField(default=0)),
                ('s5_win', models.PositiveSmallIntegerField(default=0)),
                ('s5_l', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PublicStatisticsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wins', models.PositiveSmallIntegerField(default=0)),
                ('loses', models.PositiveSmallIntegerField(default=0)),
                ('dry_wins', models.PositiveSmallIntegerField(default=0)),
                ('dry_loses', models.PositiveSmallIntegerField(default=0)),
                ('s1_win', models.PositiveSmallIntegerField(default=0)),
                ('s1_l', models.PositiveSmallIntegerField(default=0)),
                ('s2_win', models.PositiveSmallIntegerField(default=0)),
                ('s2_l', models.PositiveSmallIntegerField(default=0)),
                ('s3_win', models.PositiveSmallIntegerField(default=0)),
                ('s3_l', models.PositiveSmallIntegerField(default=0)),
                ('s4_win', models.PositiveSmallIntegerField(default=0)),
                ('s4_l', models.PositiveSmallIntegerField(default=0)),
                ('s5_win', models.PositiveSmallIntegerField(default=0)),
                ('s5_l', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
    ]
