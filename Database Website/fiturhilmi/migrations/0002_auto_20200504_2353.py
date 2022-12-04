# Generated by Django 2.2.5 on 2020-05-04 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiturhilmi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTindakan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IDKonsultasi', models.CharField(choices=[('1a', '1'), ('2a', '2'), ('3a', '3'), ('4a', '4'), ('5a', '5')], max_length=10)),
                ('IDTransaksi', models.TextField(max_length=50)),
                ('Catatan', models.TextField(max_length=100)),
                ('IDTindakanKlinik', models.TextField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='ModelStory',
        ),
    ]