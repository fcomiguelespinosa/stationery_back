# Generated by Django 3.1 on 2020-08-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
