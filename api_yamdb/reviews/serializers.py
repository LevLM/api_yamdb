from django.contrib.auth import get_user_model
from reviews.models import Comment, Review
from titles.models import Category, Genre, Title
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
# from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        # ('id', 'title_id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    post = serializers.ReadOnlyField(
        source='review.id'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Title


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category