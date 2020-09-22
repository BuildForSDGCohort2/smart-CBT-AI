# Generated by Django 3.1 on 2020-09-15 17:21

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapi', '0010_auto_20200914_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='objective',
            name='solution',
            field=models.CharField(default=False, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='objective',
            name='options',
            field=django_mysql.models.ListCharField(models.CharField(max_length=30), max_length=93, null=True, size=3),
        ),
        migrations.AlterField(
            model_name='theory',
            name='answer',
            field=django_mysql.models.ListCharField(models.CharField(max_length=30), max_length=93, size=3),
        ),
    ]
