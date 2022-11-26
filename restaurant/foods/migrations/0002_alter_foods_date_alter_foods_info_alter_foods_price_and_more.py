# Generated by Django 4.1.3 on 2022-11-26 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='foods',
            name='price',
            field=models.IntegerField(verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='rate',
            field=models.IntegerField(verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='time',
            field=models.IntegerField(verbose_name='زمان لازم برای اماده شدن'),
        ),
    ]