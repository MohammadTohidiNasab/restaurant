# Generated by Django 4.1.3 on 2022-11-26 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_foods_date_alter_foods_info_alter_foods_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='name',
            field=models.CharField(max_length=50, verbose_name='اسم'),
        ),
    ]