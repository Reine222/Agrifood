# Generated by Django 2.2.6 on 2019-12-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0007_auto_20191205_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='forme',
            field=models.CharField(default='azerty', max_length=50),
            preserve_default=False,
        ),
    ]
