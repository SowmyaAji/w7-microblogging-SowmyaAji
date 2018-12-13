from django.shortcuts import render, redirect
from chilipili.models import Chilipili

from django.conf import settings
# from django.db.models import Count
# from django.contrib import messages


def index(request):
    chilipilis = Chilipili.objects.all().order_by("-created_at")

    return render(request, 'index.html', {'chilipilis': chilipilis,
                                          })


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


# @login_required
# def like_chilipili(request, pk):

#     chilipili = get_object_or_404(Chilipili, pk=pk)
#     if request.method == "POST":
#         if not Like.objects.filter(chilipili=chilipili, like_user=request.user):
#             Like.objects.create(chilipili=chilipili, like_user=request.user)

#         else:

#             return redirect('home')
