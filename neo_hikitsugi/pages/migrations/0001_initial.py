# Generated by Django 3.2.6 on 2021-08-07 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_code', models.CharField(max_length=250)),
                ('cluster_status', models.CharField(choices=[('N', 'Not Started'), ('I', 'In Porgress'), ('C', 'Closed')], max_length=20)),
                ('jira_link', models.CharField(max_length=250)),
            ],
        ),
    ]