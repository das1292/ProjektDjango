from rest_framework import generics, permissions, filters, viewsets
from kursy.models import Kurs, Lekcja, Autor
from kursy.serializers import KursSerializer, LekcjaSerializer, AutorSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Count

class KursListCreateView(generics.ListCreateAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class KursRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class LekcjaListCreateView(generics.ListCreateAPIView):
    queryset = Lekcja.objects.all()
    serializer_class = LekcjaSerializer

class LekcjaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lekcja.objects.all()
    serializer_class = LekcjaSerializer

class AutorListCreateView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer

class KursStatsView(APIView):
    def get(self, request):
        dane = Kurs.objects.annotate(ile_lekcji=Count('lekcje')).values('nazwa', 'ile_lekcji')
        return Response(dane)

class KursViewSet(viewsets.ModelViewSet):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nazwa']
    ordering_fields = ['nazwa', 'id']

    def perform_create(self, serializer):
        autor = self.request.user.autor  # zakładamy, że user -> autor jest relacją OneToOne
        serializer.save(autor=autor)

    @action(detail=True, methods=['get'])
    def lekcje(self, request, pk=None):
        kurs = self.get_object()
        lekcje = kurs.lekcje.all()
        serializer = LekcjaSerializer(lekcje, many=True)
        return Response(serializer.data)