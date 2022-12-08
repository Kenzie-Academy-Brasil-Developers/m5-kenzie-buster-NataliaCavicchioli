from rest_framework import serializers
from users.serializers import RegisterSerializer
from .models import Movie, MovieOrder


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, allow_null=True, default=None)
    rating = serializers.ChoiceField(
        allow_null=True,
        default="G",
        choices=[
            "G",
            "PG",
            "PG-13",
            "R",
            "NC-17",
        ],
    )
    synopsis = serializers.CharField(allow_null=True, default=None)
    added_by = serializers.SerializerMethodField()

    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        return movie

    def get_added_by(self, obj):
        return obj.user.email

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance


class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.SerializerMethodField(read_only=True)
    price = serializers.DecimalField(max_digits=1000, decimal_places=2)
    buyed_by = serializers.SerializerMethodField(read_only=True)
    buyed_at = serializers.SerializerMethodField(read_only=True)

    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)

    def get_title(self, obj):
        return obj.movie.title

    def get_buyed_by(self, obj):
        return obj.user.email

    def get_buyed_at(self, obj):
        return obj.buyed_at
