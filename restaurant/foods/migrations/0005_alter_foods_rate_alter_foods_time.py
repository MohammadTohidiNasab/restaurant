# Generated by Django 4.1.3 on 2022-11-27 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_alter_foods_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='rate',
            field=models.IntegerField(default=0, verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='foods',
            name='time',
            field=models.IntegerField(verbose_name='زمان آماده شدن'),
        ),
    ]
