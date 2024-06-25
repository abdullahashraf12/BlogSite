from rest_framework import serializers
from .models import Post, Category, Tag, Comment
from userauths.models import Profile  # Import Profile from userauths app
from .permissions import IsOwnerOrReadOnly  # Import custom permission

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'  # Include all fields for Profile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# class PostSerializer(serializers.ModelSerializer):
#     # author = ProfileSerializer()  # Use ProfileSerializer to represent author
#     categories = CategorySerializer(many=True)
#     tags = TagSerializer(many=True)

#     class Meta:
#         model = Post
#         fields = '__all__'
#         read_only_fields = ['author']  # Make author read-only
#     def get_author(self, obj):
#         if obj.author.profile:
#             return ProfileSerializer(obj.author.profile).data
#         else:
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#             print(obj.author.profile)
#         return None
#     # Apply custom permission
#     def get_permissions(self):
#         if self.request.method == 'DELETE':
#             return [IsOwnerOrReadOnly()]
#         return []
from rest_framework import serializers
from .models import Post, Category, Tag
from .serializers import CategorySerializer, TagSerializer
from rest_framework.exceptions import ValidationError

class PostSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        required=False
    )
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author']  # Make author read-only

    # Custom create method to handle categories and tags
    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        tags_data = validated_data.pop('tags', [])
        
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            try:
                author_profile = request.user.profile
            except Profile.DoesNotExist:
                raise ValidationError("Profile does not exist for this user.")
            
            validated_data['author'] = author_profile
        else:
            raise ValidationError("User must be logged in.")
        
        post = Post.objects.create(**validated_data)

        for category in categories_data:
            post.categories.add(category)

        for tag in tags_data:
            post.tags.add(tag)

        return post

    # Apply custom permission
    def get_permissions(self):
        if self.context['request'].method == 'DELETE':
            return [IsOwnerOrReadOnly()]
        return []








from rest_framework.exceptions import ValidationError

from rest_framework import serializers
from .models import Comment
from .models import Profile  # Import Profile model if not already imported
from rest_framework.exceptions import ValidationError

class CommentSerializer(serializers.ModelSerializer):


    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author']  # Make author read-only for updates

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            try:
                author_profile = request.user.profile
            except Profile.DoesNotExist:
                raise ValidationError("Profile does not exist for this user.")
            
            validated_data['author'] = author_profile
        else:
            raise ValidationError("User must be logged in.")
        
        comment = Comment.objects.create(**validated_data)
        return comment
