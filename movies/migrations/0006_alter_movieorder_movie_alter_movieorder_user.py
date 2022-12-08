# Generated by Django 4.1.3 on 2022-12-08 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0005_movieorder_movie_movie_orders"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movieorder",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pivot_movie_orders",
                to="movies.movie",
            ),
        ),
        migrations.AlterField(
            model_name="movieorder",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_movie_orders",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]