# Generated by Django 3.0.4 on 2021-01-07 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('asApp', '0006_auto_20210107_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='asApp.Request'),
        ),
    ]
