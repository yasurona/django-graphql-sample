import graphene
from ..types import PlayerType
from sampleapp.models import Player

class PlayerQuery(graphene.ObjectType):
    players = graphene.List(PlayerType)
    player = graphene.Field(PlayerType, id=graphene.ID())

    def resolve_players(self, info, **kwargs):
        return Player.objects.all()

    def resolve_player(self, info, **kwargs):
        player_id = kwargs.get('id')

        if player_id:
            return Player.objects.get(id=player_id)
        else:
            return None
