# Generated by Django 2.2.3 on 2020-08-06 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200806_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
    ]
