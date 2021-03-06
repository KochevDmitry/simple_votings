# Generated by Django 3.1.4 on 2020-12-22 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformationAboutVoting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information', models.TextField()),
                ('labels', models.TextField()),
                ('voting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.votings')),
            ],
        ),
    ]
