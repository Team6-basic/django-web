from django.db import models


class Day_Hate(models.Model):
    id = models.AutoField(primary_key=True)
    rec_date = models.DateField()
    user_id = models.IntegerField()


class Time_Hate(models.Model):
    id = models.AutoField(primary_key=True)
    rec_datetime = models.DateTimeField()
    user_id = models.IntegerField()
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
