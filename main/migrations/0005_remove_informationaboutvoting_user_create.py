# Generated by Django 3.1.4 on 2021-01-16 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_informationaboutvoting_user_create'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='informationaboutvoting',
            name='user_create',
        ),
    ]