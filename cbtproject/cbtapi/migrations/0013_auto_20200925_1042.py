# Generated by Django 3.1.1 on 2020-09-25 17:42

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapi', '0012_auto_20200915_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='options',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=404, size=4),
        ),
        migrations.AlterField(
            model_name='theory',
            name='answer',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), max_length=303, size=3),
        ),
        migrations.AlterField(
            model_name='theory',
            name='question',
            field=models.CharField(max_length=300),
        ),
    ]