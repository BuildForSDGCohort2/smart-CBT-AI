# Generated by Django 3.1 on 2020-09-22 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_auto_20200922_0932'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result_Theory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('isCorrect', models.BooleanField()),
            ],
        ),
    ]
