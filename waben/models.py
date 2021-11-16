from django.db import models
from django.contrib.auth.models import User
   
class Oder(models.Model):
    name = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    username = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    dining = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    month = models.IntegerField(
        blank=True,
        null=True,
    )
    day1 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day2 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day3 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day4 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day5 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day6 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day7 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day8 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day9 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day10 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day11 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day12 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day13 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day14 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day15 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day16 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day17 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day18 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day19 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day20 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day21 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day22 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day23 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day24 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day25 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day26 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day27 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day28 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day29 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day30 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    day31 = models.CharField(
        max_length=32,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.name.username