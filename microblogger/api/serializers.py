from rest_framework import serializers
from chilipili.models import Chilipili, User, Follow, Like


class CreatableSlugRelatedField(serializers.SlugRelatedField):
    def to_internal_value(self, data):
        try:
            value, _ = self.get_queryset().get_or_create(
                **{self.slug_field: data})
            return value
        except (TypeError, ValueError):
            self.fail("invalid")


class ChilipiliSerializer(serializers.ModelSerializer):

    author_user = serializers.SlugRelatedField(
        slug_field="username", read_only=True)
    text = serializers.CharField(max_length=280)

    # created_at = serializers.DateTimeField()

    class Meta:
        model = Chilipili
        fields = ("author_user", "text", )


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
