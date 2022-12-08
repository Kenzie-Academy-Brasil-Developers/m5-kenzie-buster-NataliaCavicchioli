from django.db import models
from users.models import User


class RatingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True, default=None)
    rating = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=RatingChoices.choices,
        default=RatingChoices.G,
    )
    synopsis = models.TextField(null=True, blank=True, default=None)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="movies",
    )
    orders = models.ManyToManyField(
        "users.User",
        through="movies.MovieOrder",
        related_name="movies_orders",
    )

    def __repr__(self) -> str:
        return f"<Movie [{self.id}] - {self.title}>"


class MovieOrder(models.Model):
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="pivot_movie_orders"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_movie_orders"
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=1000, decimal_places=2)

    def __repr__(self) -> str:
        return f"<MovieOrder [{self.id}] - {self.movie.title} & {self.user.username}>"
