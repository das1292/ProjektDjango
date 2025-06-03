from rest_framework import generics, permissions
from kursy.models import Kurs, Lekcja, Autor
from kursy.serializers import KursSerializer, LekcjaSerializer, AutorSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
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
