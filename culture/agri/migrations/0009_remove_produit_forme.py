# Generated by Django 2.2.6 on 2019-12-05 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0008_auto_20191205_1638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='forme',
        ),
    ]
