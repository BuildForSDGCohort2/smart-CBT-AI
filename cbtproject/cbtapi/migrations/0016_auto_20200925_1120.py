# Generated by Django 3.1.1 on 2020-09-25 18:20

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapi', '0015_auto_20200925_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theory',
            name='answer',
            field=django_mysql.models.ListTextField(models.CharField(max_length=500, null=True), null=True, size=None),
        ),
    ]
