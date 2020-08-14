# Generated by Django 3.0.7 on 2020-08-14 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Charecter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charecter_name', models.CharField(max_length=50)),
                ('player_name', models.CharField(max_length=50)),
                ('img_url', models.CharField(max_length=200)),
                ('team', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='charecters.Team')),
            ],
        ),
    ]
