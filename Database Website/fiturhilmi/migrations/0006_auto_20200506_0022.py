# Generated by Django 2.2.5 on 2020-05-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiturhilmi', '0005_auto_20200506_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modeltindakan',
            name='IDKonsultasi',
            field=models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=10),
        ),
    ]
