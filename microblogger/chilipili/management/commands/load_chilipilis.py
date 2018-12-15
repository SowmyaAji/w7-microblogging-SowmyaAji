from django.core.management.base import BaseCommand
from mimesis import Person
from chilipili.models import Chilipili, User, Like, Follow
from mimesis import Person, Text
from random import choice


class Command(BaseCommand):
    help = "load chilipilis and users dynamically"

    def add_arguments(self, parser):
        # parser.add_argument('sample', nargs='+')
        pass

    def handle(self, *args, **options):
        Chilipili.objects.all().delete()
        Like.objects.all().delete()
        users = []
        person = Person()
        for _ in range(10):
            User.objects.create(password=person.password(), username=person.username(
            ), first_name=person.name(), last_name=person.last_name(), email=person.email())
        # date = Datetime()
        text = Text()
        users = User.objects.all()
        for _ in range(20):
            Chilipili.objects.create(author_user=choice(
                users), text=text.sentence())

        chilipilis = Chilipili.objects.all()
        for _ in range(100):
            Like.objects.create(like_user=choice(
                users), chilipili=choice(chilipilis))
