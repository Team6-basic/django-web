from django.db import models


class Device(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    rp_serial = models.CharField(max_length=30)


class Day_Hate(models.Model):
    id = models.AutoField(primary_key=True)
    rec_date = models.DateField()
    user_id = models.IntegerField(null=False)


class Time_Hate(models.Model):
    id = models.AutoField(primary_key=True)
    rec_datetime = models.DateTimeField()
    user_id = models.IntegerField(null=False)
    fg_none = models.FloatField()
    fg_other_hate = models.FloatField()
    fg_man = models.FloatField()
    fg_normal_bad_comments = models.FloatField()
    fg_sexual_minority = models.FloatField()
    fg_woman_or_family = models.FloatField()
    fg_age = models.FloatField()
    fg_race_or_nationality = models.FloatField()
    fg_religion = models.FloatField()
    fg_region = models.FloatField()
    speech = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
