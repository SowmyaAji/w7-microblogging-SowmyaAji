from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    users_followed = models.ManyToManyField(
        to="User",
        through="Follow",
        through_fields=("following_user", "followed_user"),
        related_name="followers",
    )


# class Chilipili(models.Model):
#     author_user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="chilipilis")
#     text = models.TextField(min_length=2, max_length=280)
#     created_at = models.DateTimeField(auto_now=True)
#     updated_at = models.DateTimeField(auto_now_add=True)


# class Like(models.Model):
#     chilipili = models.ForeignKey(
#         to="Chilipili", on_delete=models.CASCADE, null=True, related_name="likes")
#     like_user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="likes")


# class Follow(models.Model):
#     following_user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follows_from")
#     followed_user = models.ForeignKey(
#         settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follows_to")


# class Repost(models.Model):
#     repost_user = models.ForeignKey(
#         to="User", on_delete=models.CASCADE, related_name="reposts")
#     chilipili = models.ForeignKey(
#         to="Chilipili", on_delete=models.CASCADE, null=True, related_name="reposts")
#     date = models.DateTimeField(auto_now=True)
