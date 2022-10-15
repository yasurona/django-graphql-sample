import graphene
from sampleapp.schema.schema import SampleappQuery

class Query(SampleappQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
