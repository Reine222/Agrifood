# Generated by Django 2.2.6 on 2019-12-06 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0009_remove_produit_forme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panier',
            name='forme',
        ),
    ]