import graphene
from .queries import PlayerQuery

class SampleappQuery(PlayerQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=SampleappQuery)
