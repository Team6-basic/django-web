# Generated by Django 4.2.2 on 2023-06-16 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day_Hate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Time_Hate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(null=True)),
                ('label1', models.FloatField(blank=True, null=True, verbose_name='여성/가족')),
                ('label2', models.FloatField(blank=True, null=True, verbose_name='남성')),
                ('label3', models.FloatField(blank=True, null=True, verbose_name='성소수자')),
                ('label4', models.FloatField(blank=True, null=True, verbose_name='인종/국적')),
                ('label5', models.FloatField(blank=True, null=True, verbose_name='연령')),
                ('label6', models.FloatField(blank=True, null=True, verbose_name='지역')),
                ('label7', models.FloatField(blank=True, null=True, verbose_name='종교')),
                ('label8', models.FloatField(blank=True, null=True, verbose_name='기타혐오')),
                ('label9', models.FloatField(blank=True, null=True, verbose_name='악플/욕설')),
                ('label10', models.FloatField(blank=True, null=True, verbose_name='clean')),
                ('rec_day', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hopecharm.day_hate')),
            ],
        ),
    ]
