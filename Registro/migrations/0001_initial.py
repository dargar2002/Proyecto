# Generated by Django 4.0.6 on 2022-08-31 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carnet', models.CharField(max_length=6)),
                ('full_name', models.CharField(max_length=40)),
                ('direction', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
                ('phone_num', models.IntegerField(max_length=8)),
                ('date_birth', models.DateField()),
                ('career', models.CharField(max_length=50)),
                ('tpoetry', models.CharField(max_length=15)),
                ('date', models.DateField()),
            ],
        ),
    ]
