# Generated by Django 3.1.4 on 2021-01-16 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_informationaboutvoting_user_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationaboutvoting',
            name='user_create',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
