# Generated by Django 4.1.3 on 2022-11-26 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_alter_foods_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foods',
            name='info',
            field=models.CharField(max_length=100, verbose_name='توضیحات'),
        ),
    ]
