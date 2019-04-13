# Generated by Django 2.1.7 on 2019-04-13 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190413_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='header',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_set', to='main.Question'),
        ),
    ]