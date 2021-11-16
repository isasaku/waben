# Generated by Django 3.2.7 on 2021-11-14 11:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=32, null=True)),
                ('dining', models.CharField(blank=True, max_length=32, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('day1', models.CharField(blank=True, max_length=32, null=True)),
                ('day2', models.CharField(blank=True, max_length=32, null=True)),
                ('day3', models.CharField(blank=True, max_length=32, null=True)),
                ('day4', models.CharField(blank=True, max_length=32, null=True)),
                ('day5', models.CharField(blank=True, max_length=32, null=True)),
                ('day6', models.CharField(blank=True, max_length=32, null=True)),
                ('day7', models.CharField(blank=True, max_length=32, null=True)),
                ('day8', models.CharField(blank=True, max_length=32, null=True)),
                ('day9', models.CharField(blank=True, max_length=32, null=True)),
                ('day10', models.CharField(blank=True, max_length=32, null=True)),
                ('day11', models.CharField(blank=True, max_length=32, null=True)),
                ('day12', models.CharField(blank=True, max_length=32, null=True)),
                ('day13', models.CharField(blank=True, max_length=32, null=True)),
                ('day14', models.CharField(blank=True, max_length=32, null=True)),
                ('day15', models.CharField(blank=True, max_length=32, null=True)),
                ('day16', models.CharField(blank=True, max_length=32, null=True)),
                ('day17', models.CharField(blank=True, max_length=32, null=True)),
                ('day18', models.CharField(blank=True, max_length=32, null=True)),
                ('day19', models.CharField(blank=True, max_length=32, null=True)),
                ('day20', models.CharField(blank=True, max_length=32, null=True)),
                ('day21', models.CharField(blank=True, max_length=32, null=True)),
                ('day22', models.CharField(blank=True, max_length=32, null=True)),
                ('day23', models.CharField(blank=True, max_length=32, null=True)),
                ('day24', models.CharField(blank=True, max_length=32, null=True)),
                ('day25', models.CharField(blank=True, max_length=32, null=True)),
                ('day26', models.CharField(blank=True, max_length=32, null=True)),
                ('day27', models.CharField(blank=True, max_length=32, null=True)),
                ('day28', models.CharField(blank=True, max_length=32, null=True)),
                ('day29', models.CharField(blank=True, max_length=32, null=True)),
                ('day30', models.CharField(blank=True, max_length=32, null=True)),
                ('day31', models.CharField(blank=True, max_length=32, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
