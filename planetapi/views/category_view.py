"""View module for handling requests about categories"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from planetapi.models import Category


class CategoryView(ViewSet):
    def retrieve(self, request, pk):
        """Handle GET requests for single category

        Returns:
            Response -- JSON serialized category
        """
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for categories
    """
    class Meta:
        model = Category
        fields = ('id', 'label',)