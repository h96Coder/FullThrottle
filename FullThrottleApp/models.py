from django.db import models


class User(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    real_name = models.CharField(max_length=100)
    tz = models.CharField(max_length=100)


class ActivityPeriod(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    start_time = models.CharField(max_length=100)
    end_time = models.CharField(max_length=100)


# Create your models here.

