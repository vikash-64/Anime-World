# Generated by Django 4.0.4 on 2022-05-12 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothingApp', '0002_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='second',
            field=models.URLField(blank=True, null=True),
        ),
    ]