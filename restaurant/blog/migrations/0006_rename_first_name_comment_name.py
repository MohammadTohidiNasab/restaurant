# Generated by Django 4.1.3 on 2022-12-18 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_created_at_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='first_name',
            new_name='name',
        ),
    ]
