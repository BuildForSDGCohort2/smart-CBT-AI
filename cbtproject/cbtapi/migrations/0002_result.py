# Generated by Django 3.1 on 2020-09-03 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.CharField(max_length=60)),
                ('questions', models.ManyToManyField(related_name='_result_questions_+', to='cbtapi.Result')),
            ],
        ),
    ]
