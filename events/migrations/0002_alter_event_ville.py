# Generated by Django 4.2 on 2023-06-23 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ville',
            field=models.CharField(default='Your Default city', max_length=100),
        ),
    ]
