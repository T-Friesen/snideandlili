from rest_framework import serializers
from .models import BlogPost, Tag, Category, Author

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    categories = CategorySerializer(many=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
        
class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Author
        fields = ['id', 'user', 'bio']