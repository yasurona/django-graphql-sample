from graphene_django import DjangoObjectType
from sampleapp.models import Country

class CountryType(DjangoObjectType):
    class Meta:
        model = Country
