from django.contrib import admin

from django.contrib import admin
from chilipili.models import Chilipili, Like, Follow, User


class ChilipiliAdmin(admin.ModelAdmin):
    model = Chilipili
    list_display = ('author_user', 'text', )


class UserAdmin(admin.ModelAdmin):
    model = User


admin.site.register(Chilipili, ChilipiliAdmin)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(User, UserAdmin)
