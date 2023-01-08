# Generated by Django 4.1.3 on 2022-12-18 07:51

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_alter_blog_category_blog_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='تاریخ ایجاد'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='نام کاربر')),
                ('email', models.EmailField(max_length=254, verbose_name='ادرس الکترونیکی')),
                ('massage', models.TextField(verbose_name='متن نظر')),
                ('date', models.DateField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog', verbose_name='مقاله')),
            ],
        ),
    ]