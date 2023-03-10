# Generated by Django 4.1.5 on 2023-01-30 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_transition', models.CharField(max_length=1)),
                ('date', models.DateField()),
                ('value', models.FloatField()),
                ('cpf', models.IntegerField()),
                ('card', models.IntegerField()),
                ('hour', models.TimeField()),
                ('market_owner', models.CharField(max_length=14)),
                ('market_name', models.CharField(max_length=19)),
            ],
        ),
    ]
