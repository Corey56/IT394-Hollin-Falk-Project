# Generated by Django 3.0.3 on 2020-05-04 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codhc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='desc',
            new_name='comment_text',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='desc',
            new_name='post_text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_at',
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date published'),
        ),
    ]