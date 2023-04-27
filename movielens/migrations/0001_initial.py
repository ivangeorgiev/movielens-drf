# Generated by Django 4.2 on 2023-04-27 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("movie_id", models.BigAutoField(primary_key=True, serialize=False)),
                ("title", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="MovieLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("imdb_id", models.CharField(max_length=255, null=True)),
                ("themoviedb_id", models.CharField(max_length=255, null=True)),
                (
                    "movie",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links",
                        to="movielens.movie",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="MovieGenre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genre", models.CharField(max_length=32)),
                (
                    "movie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="genres",
                        to="movielens.movie",
                    ),
                ),
            ],
        ),
    ]
