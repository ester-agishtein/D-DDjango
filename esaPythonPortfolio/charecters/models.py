from django.db import models
from enum import IntEnum
# Create your models here.


class Charecter(models.Model):
    NEUTRAL = "neutral"
    LAWFUL = "lawful"
    CHAOTIC = "chaotic"

    GOOD = "good"
    EVIL = "evil"
    ALIGNEMENT_CHOICES = (
        (GOOD, "good"),
        (EVIL, "evil"),
    )
    ORIENTATION_CHOICES = (
        (NEUTRAL, "neutral"),
        (LAWFUL, "lawful"),
        (CHAOTIC, "chaotic"),
    )

    charecter_name = models.CharField(max_length=50)
    player_name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=200)
    team = models.ForeignKey("Team",  on_delete=models.CASCADE, blank=False)
    class_type = models.CharField(
        verbose_name="class", max_length=50, blank=True)
    race = models.CharField(max_length=50, blank=True)
    hit_points = models.IntegerField(default=5)
    armor_class = models.IntegerField(default=5)
    orientation = models.CharField(
        max_length=10,
        choices=ORIENTATION_CHOICES, default=NEUTRAL)
    alignment = models.CharField(
        max_length=10,
        choices=ALIGNEMENT_CHOICES, default=GOOD)
    notes = models.TextField(blank=True, max_length=800)

    def __str__(self):
        return self.charecter_name


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    notes = models.TextField(blank=True, max_length=800)

    def __str__(self):
        return self.team_name
