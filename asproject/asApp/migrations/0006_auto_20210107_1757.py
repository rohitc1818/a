# Generated by Django 3.0.4 on 2021-01-07 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asApp', '0005_update_request'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='request',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='asApp.Request'),
        ),
    ]