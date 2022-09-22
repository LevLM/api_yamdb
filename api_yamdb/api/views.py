# # from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404

from api_yamdb.api.permissions import IsAdminOrReadOnly
from api_yamdb.reviews.models import Review
from rest_framework import viewsets
# permissions
# filters, mixins,
# from rest_framework.pagination import LimitOffsetPagination

# from .permissions import OwnerOrReadOnly
from api_yamdb.api.serializers import (ReviewSerializer, CommentSerializer,
                                       TitleSerializer, CategorySerializer,
                                       GenreSerializer)
from api_yamdb.titles.models import Title, Category, Genre


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     # OwnerOrReadOnly,
    # )
    # pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    # permission_classes = (
    #     permissions.IsAuthenticatedOrReadOnly,
    #     # OwnerOrReadOnly,
    # )

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [IsAdminOrReadOnly, ]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly, ]


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAdminOrReadOnly, ]