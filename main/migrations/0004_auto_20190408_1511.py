# Generated by Django 2.1.7 on 2019-04-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190408_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='date_last_report',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='date_last_report',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
