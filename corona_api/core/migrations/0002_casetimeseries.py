# Generated by Django 2.2.7 on 2020-09-13 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseTimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_confirmed', models.IntegerField()),
                ('daily_deceased', models.IntegerField()),
                ('daily_recovered', models.IntegerField()),
                ('total_confirmed', models.IntegerField()),
                ('total_deceased', models.IntegerField()),
                ('total_recovered', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
