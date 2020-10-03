# Generated by Django 3.1.1 on 2020-09-25 17:57

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapi', '0013_auto_20200925_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objective',
            name='answer',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='objective',
            name='options',
            field=django_mysql.models.ListCharField(models.CharField(max_length=100), max_length=404, null=True, size=4),
        ),
        migrations.AlterField(
            model_name='objective',
            name='question',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='objective',
            name='solution',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='theory',
            name='answer',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), max_length=303, null=True, size=3),
        ),
        migrations.AlterField(
            model_name='theory',
            name='question',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='theory',
            name='solution',
            field=models.TextField(null=True),
        ),
    ]
