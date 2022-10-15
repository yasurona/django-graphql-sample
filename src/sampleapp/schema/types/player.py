from graphene_django import DjangoObjectType
from sampleapp.models import Player

class PlayerType(DjangoObjectType):
    class Meta:
        model = Player
