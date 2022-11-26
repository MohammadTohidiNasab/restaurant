# Generated by Django 4.1.3 on 2022-11-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Foods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('info', models.TextField(max_length=100)),
                ('price', models.IntegerField()),
                ('date', models.DateTimeField(verbose_name='تاریخ ثبت')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='زمان لازم برای اماده شدن')),
                ('photo', models.ImageField(upload_to='food_images/')),
                ('rate', models.ImageField(upload_to='')),
            ],
        ),
    ]
