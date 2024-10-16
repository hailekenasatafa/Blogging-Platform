from rest_framework.exceptions import ValidationError

def validate(self, data):
    if not data['title']:
        raise ValidationError("Title is required")
    return data
from django_filters.rest_framework import DjangoFilterBackend
class BlogPostViewSet(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'author']
