from django.db import models


class Day_Hate(models.Model):
    id = models.AutoField(primary_key=True)
    rec_date = models.DateField()
    user_id = models.IntegerField()


class Time_Hate(models.Model):
    id = models.AutoField(primary_key=True)
    rec_datetime = models.DateTimeField()

    fg_woman_or_family = models.FloatField(verbose_name="여성/가족")
    fg_man = models.FloatField(verbose_name="남성")
    fg_sexual_minority = models.FloatField(verbose_name="성소수자")
    fg_race_or_nationality = models.FloatField(verbose_name="인종/국적")
    fg_age = models.FloatField(verbose_name="연령")
    fg_region = models.FloatField(verbose_name="지역")
    fg_religion = models.FloatField(verbose_name="종교")
    fg_other_hate = models.FloatField(verbose_name="기타혐오")
    fg_normal_bad_comments = models.FloatField(verbose_name="악플/욕설")
    fg_none = models.FloatField(verbose_name="clean")

    speech = models.TextField()
    user_id = models.IntegerField()
