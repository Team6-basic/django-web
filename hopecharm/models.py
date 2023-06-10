# Create your models here.
from django.db import models

# Create your models here.
class Day_Hate(models.Model):
    rec_date = models.DateField()

class Time_Hate(models.Model):
    rec_day = models.ForeignKey(Day_Hate, on_delete=models.CASCADE) 
    # 상위 분류인 Day_Hate 의 날짜가 지워지면 아래 시간별 분류인 Time_Hate도 삭제되도록!

    create_time = models.DateTimeField()
    label1 = models.IntegerField(verbose_name="여성/가족")
    label2 = models.IntegerField(verbose_name="남성")
    label3 = models.IntegerField(verbose_name="성소수자")
    label4 = models.IntegerField(verbose_name="인종/국적")
    label5 = models.IntegerField(verbose_name="연령")
    label6 = models.IntegerField(verbose_name="지역")
    label7 = models.IntegerField(verbose_name="종교")
    label8 = models.IntegerField(verbose_name="기타혐오")
    label9 = models.IntegerField(verbose_name="악플/욕설")
    label10 = models.IntegerField(verbose_name="clean")

# pd.date_range('2019-11-25 09:00:00', '2019-11-25 16:00:00', freq='10min')