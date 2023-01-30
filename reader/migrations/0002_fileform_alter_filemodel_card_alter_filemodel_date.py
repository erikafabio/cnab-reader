# Generated by Django 4.1.5 on 2023-01-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='card',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='filemodel',
            name='date',
            field=models.CharField(max_length=16),
        ),
    ]