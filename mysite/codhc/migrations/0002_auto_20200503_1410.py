# Generated by Django 3.0.3 on 2020-05-03 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codhc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
