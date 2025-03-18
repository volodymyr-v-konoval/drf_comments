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
