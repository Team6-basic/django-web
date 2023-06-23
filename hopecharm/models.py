from django.db import models
from django.db.models import Avg, Count, Min, Sum
from django.conf import settings

class Day_Hate(models.Model):
    rec_date = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.rec_date}, {self.user}"

class Time_Hate(models.Model):
    create_time = models.DateTimeField(null=True)
    label1 = models.FloatField(blank=True, null=True, verbose_name="여성/가족")
    label2 = models.FloatField(blank=True, null=True, verbose_name="남성")
    label3 = models.FloatField(blank=True, null=True, verbose_name="성소수자")
    label4 = models.FloatField(blank=True, null=True, verbose_name="인종/국적")
    label5 = models.FloatField(blank=True, null=True, verbose_name="연령")
    label6 = models.FloatField(blank=True, null=True, verbose_name="지역")
    label7 = models.FloatField(blank=True, null=True, verbose_name="종교")
    label8 = models.FloatField(blank=True, null=True, verbose_name="기타혐오")
    label9 = models.FloatField(blank=True, null=True, verbose_name="악플/욕설")
    label10 = models.FloatField(blank=True, null=True, verbose_name="clean")

    rec_day = models.ForeignKey(Day_Hate, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.rec_day}, {self.create_time}"
