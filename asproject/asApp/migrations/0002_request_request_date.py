# Generated by Django 3.0.4 on 2021-01-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='Request_Date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
