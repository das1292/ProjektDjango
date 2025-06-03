import graphene
from graphene_django.types import DjangoObjectType
from kursy.models import Kurs, Lekcja, Autor
from django.db.models import Count

class KursType(DjangoObjectType):
    lekcja_count = graphene.Int()
    class Meta:
        model = Kurs
    def resolve_lekcja_count(self, info):
        return self.lekcje.count()

class LekcjaType(DjangoObjectType):
    class Meta:
        model = Lekcja

class AutorType(DjangoObjectType):
    class Meta:
        model = Autor

class Query(graphene.ObjectType):
    all_kursy = graphene.List(KursType)
    moje_kursy = graphene.List(KursType)

    def resolve_all_kursy(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Użytkownik niezalogowany.")
        return Kurs.objects.annotate(lekcja_count=Count('lekcje'))

    def resolve_moje_kursy(self, info):
        user = info.context.user
        if not user.is_authenticated:
            raise Exception("Użytkownik niezalogowany.")
        try:
            autor = Autor.objects.get(user=user)
        except Autor.DoesNotExist:
            raise Exception("Brak powiązanego autora.")
        return Kurs.objects.filter(autor=autor).annotate(lekcja_count=Count('lekcje'))

schema = graphene.Schema(query=Query)