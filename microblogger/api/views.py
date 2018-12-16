from django.shortcuts import render

from chilipili.models import Chilipili, Follow, User, Like
from api.serializers import ChilipiliSerializer, FollowSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


class ChilipiliListCreateView(generics.ListCreateAPIView):
    serializer_class = ChilipiliSerializer

    def get_queryset(self):
        return self.request.user.chilipilis

    def perform_create(self, serializer):
        serializer.save(author_user=self.request.user)


class ChilipiliRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChilipiliSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return self.request.user.chilipilis


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class FollowListCreateView(generics.ListCreateAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        return self.request.user.follows_from

    def perform_create(self, serializer):
        serializer.save(following_user=self.request.user)


class FollowDestroyView(generics.DestroyAPIView):
    lookup_field = "followed_user__username"
    lookup_url_kwarg = "username"

    def get_queryset(self):
        return self.request.user.follows_from
