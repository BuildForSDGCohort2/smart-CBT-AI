# Generated by Django 3.1 on 2020-09-22 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbtapi', '0012_auto_20200915_1139'),
        ('result', '0007_auto_20200922_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='result_obj',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cbtapi.objective'),
        ),
        migrations.AddField(
            model_name='result_theory',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cbtapi.theory'),
        ),
    ]
