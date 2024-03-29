# Generated by Django 4.0.4 on 2022-05-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(blank=True, null=True)),
                ('youtube', models.URLField(blank=True, null=True)),
                ('twitter', models.URLField(blank=True, null=True)),
                ('first', models.URLField(blank=True, null=True)),
                ('second', models.UUIDField(blank=True, null=True)),
            ],
        ),
    ]
