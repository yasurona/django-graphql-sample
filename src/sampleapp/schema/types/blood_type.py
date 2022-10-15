from graphene_django import DjangoObjectType
from sampleapp.models import BloodType

class BloodTypeType(DjangoObjectType):
    class Meta:
        model = BloodType
