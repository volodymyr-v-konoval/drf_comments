from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Comment
from captcha.serializers import CaptchaModelSerializer

class CommentSerializer(CaptchaModelSerializer):
    username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    email = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()
    sender = serializers.EmailField(write_only=True, required=False)  

    class Meta:
        model = Comment
        fields = (
            "id",
            "author",
            "username",
            "email",
            "text",
            "homepage",
            "created",
            "updated",
            "parent",
            "captcha_code",
            "captcha_hashkey",
            "sender",
        )
    
    def create(self, validated_data):
        validated_data.pop("captcha_code", None)
        validated_data.pop("captcha_hashkey", None)
        validated_data.pop("sender", None)
        
        return super().create(validated_data)

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
