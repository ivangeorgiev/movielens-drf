import csv
from dataclasses import dataclass

from django.core.management.base import BaseCommand, CommandError

from movielens.models import Movie, MovieGenre, MovieLink


@dataclass(frozen=True)
class MovieRow:
    movieId: str
    title: str
    genres: str


@dataclass(frozen=True)
class LinkRow:
    movieId: str
    imdbId: str
    tmdbId: str


def assert_empty(model):
    if model.objects.all().count() > 0:
        raise CommandError(
            f"{model.__qualname__} table '{model.objects.model._meta.db_table}' is not empty. Use --force or manually truncate the table first."
        )


def truncate_model(model):
    model.objects.all().delete()


def import_movies(datafile):
    reader = csv.reader(datafile)
    columns = next(reader)

    for row in reader:
        movie_record = MovieRow(**dict(zip(columns, row)))
        movie = Movie.objects.create(
            pk=int(movie_record.movieId),
            title=movie_record.title,
        )
        insert_movie_genres(movie, movie_record.genres)


def import_links(datafile):
    reader = csv.reader(datafile)
    columns = next(reader)

    for row in reader:
        link = LinkRow(**dict(zip(columns, row)))
        MovieLink.objects.create(
            movie_id=int(link.movieId),
            imdb_id=link.imdbId,
            themoviedb_id=link.tmdbId,
        )


def insert_movie_genres(movie, genres):
    if not genres or genres == "(no genres listed)":
        return
    MovieGenre.objects.bulk_create(
        [MovieGenre(movie_id=movie.pk, genre=genre) for genre in genres.split("|")]
    )


class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument(
            "--force", action="store_true", help="Truncate target table before load."
        )
        parser.add_argument("target", choices=["movies", "links"], type=str)
        parser.add_argument("datafile", nargs="?", type=str)

    def handle(self, *args, **options):
        target = options["target"]
        file_path = options["datafile"]
        is_forced = options["force"]

        if target == "movies":
            handle_target(Movie, file_path, is_forced)
        elif target == "links":
            handle_target(MovieLink, file_path, is_forced)
        else:
            raise CommandError(f"Unknown import target '{target}'")


def handle_target(model, file_path, truncate_first):
    importers = {
        Movie: import_movies,
        MovieLink: import_links,
    }
    if truncate_first:
        truncate_model(model)
    assert_empty(model)
    if file_path:
        with open(file_path, "r", encoding="utf8") as file:
            importers[model](file)
