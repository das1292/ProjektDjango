from rest_framework import serializers
from .models import Kurs, Lekcja, Autor

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class KursSerializer(serializers.ModelSerializer):
    lekcja_count = serializers.SerializerMethodField()
    class Meta:
        model = Kurs
        fields = '__all__'

    def get_lekcja_count(self, obj):
        return obj.lekcje.count()

class LekcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lekcja
        fields = '__all__'