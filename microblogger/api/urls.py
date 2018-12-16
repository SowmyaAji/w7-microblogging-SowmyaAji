from django.urls import path
from api import views as api_views


urlpatterns = [
    path("chilipilis/", api_views.ChilipiliListCreateView.as_view(),
         name="api_book_list"),
    path(
        "chilipilis/<pk>/",
        api_views.ChilipiliRetrieveUpdateDestroyView.as_view(),
        name="api_book",
    ),
    path("users/", api_views.UserListView.as_view(), name="api_user_list"),
    path("follows/", api_views.FollowListCreateView.as_view(),
         name="api_follow_list"),
    path(
        "follows/<str:username>/",
        api_views.FollowDestroyView.as_view(),
        name="api_follow",
    ),
]
