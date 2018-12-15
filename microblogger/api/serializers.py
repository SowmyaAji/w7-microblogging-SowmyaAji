from rest_framework import serializers
from chilipili.models import Chilipili, User, Follow, Like


class ChilipiliSerializer(serializers.ModelSerializer):

    author_user = serializers.SlugRelatedField(
        slug_field="username", read_only=True)
    text = serializers.CharField(max_length=280)

    created_at = serializers.DateTimeField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class FollowSerializer(serializers.ModelSerializer):
    followed_user = serializers.SlugRelatedField(
        slug_field="username", queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ("followed_user",)
