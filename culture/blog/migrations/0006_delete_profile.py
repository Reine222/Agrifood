# Generated by Django 2.2.6 on 2019-11-15 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]