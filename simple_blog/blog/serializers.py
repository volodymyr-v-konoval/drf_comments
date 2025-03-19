from django.contrib.auth.models import User
from rest_framework import serializers
from drf_recaptcha.fields import ReCaptchaV3Field
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(default=serializers.CurrentUserDefault())
    recaptcha = ReCaptchaV3Field(action='example', required_score=0.6)

    class Meta:
        model = Comment
        fields = ('__all__')

    def validate(self, attrs):
        attrs.pop('recaptcha')
        return attrs
    

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
