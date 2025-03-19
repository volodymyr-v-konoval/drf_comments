from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    email = serializers.SerializerMethodField()

    author = serializers.SerializerMethodField()  

    class Meta:
        model = Comment
        fields = ('__all__')
        

    def get_email(self, obj):
        return obj.username.email
    
    def get_author(self, obj):
        return obj.username.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user
