from django.shortcuts import render, redirect
from chilipili.models import Chilipili, User, Like, Follow
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import Count
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
# from django.db.models import Q
# from django.contrib import messages


def index(request):
    chilipilis = Chilipili.objects.all().order_by("-created_at")

    return render(request, 'index.html', {'chilipilis': chilipilis,
                                          })


def like_chilipili(request, pk):
    chilipili = get_object_or_404(Chilipili, pk=pk)
    if request.method == "POST":
        if not Like.objects.filter(chilipili=chilipili, like_user=request.user):
            Like.objects.create(chilipili=chilipili, like_user=request.user)
        return JsonResponse({"chilipili_pk": chilipili.id, "likes": chilipili.likes.count()})


def follow_user(request, pk):
    breakpoint()
    followed_user = get_object_or_404(
        User.objects.exclude(request.user), pk=pk)
    if request.method == 'POST':
        if not Follow.objects.filter(followed_user=followed_user, following_user=request.user):
            Follow.objects.create(followed_user=followed_user,
                                  following_user=request.user)
        return JsonResponse({"followed_user.pk": followed_user.id, "followers": followed_user.follows.count})


def sort_liked_chilipilis(request, chilipilis):
    liked_chilipilis = []
    if request.user.is_authenticated:
        liked_chilipilis = request.user.liked_chilipilis.all()
    chilipilis = chilipilis.order_by('-created_at')
    return render(request,
                  'index.html', {"chilipilis": chilipilis, "liked_chilipilis": liked_chilipilis})


@login_required
def liked_index(request):
    chilipilis = request.user.liked_chilipilis(all)
    return render(request, 'My liked chilipilis', chilipilis)


def follow_user(request, pk):
    followed_user = User.objects.exclude(request.user)
    if request.method == 'POST':
        if request.user != followed_user:
            if not Follow.objects.filter(followed_user=followed_user, following_user=request.user):
                Follow.objects.create(followed_user=followed_user,
                                      following_user=request.user)
            return JsonResponse({"followed_user.pk": followed_user.id, "followers": followed_user.follows.count})

# @login_required
# def new_chilipili(request):

#     form = PostForm(request.POST)
#     if request.method == "POST":
#         if form.is_valid():
#             new_chilipili = form.save(commit=False)
#             new_chilipili.author = request.user
#             new_chilipili.save()

#             return redirect('home')
#         else:
#             form = PostForm()

#         return render(request, 'chilipili/new_chilipili.html', {'form': form})


# @login_required
# def delete_new_chilipili(request):
#     if request.POST.get('pk'):
#         chilipili = get_object_or_404(Chilipili, pk=request.POST.get('pk'))
#         if chilipili.author == request.user:
#             chilipili.delete()

#         else:
#             return redirect('home')
