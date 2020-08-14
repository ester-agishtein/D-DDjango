from django.db import models

# Create your models here.


class Charecter(models.Model):
    charecter_name = models.CharField(max_length=50)
    player_name = models.CharField(max_length=50)
    img_url = models.CharField(max_length=200)
    team = models.ForeignKey("Team",  on_delete=models.CASCADE, blank=False)
    class_type = models.CharField(max_length=50, blank=True)
    race = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.charecter_name


class Team(models.Model):
    team_name = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name
