# Generated by Django 3.2.6 on 2021-08-11 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_post_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]