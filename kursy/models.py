from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autorzy"
    def __str__(self):
        return self.user.username

class Kurs(models.Model):
    TYP = [('O', 'Online'), ('S', 'Stacjonarny')]
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()
    typ = models.CharField(max_length=1, choices=TYP)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='kursy')
    class Meta:
        verbose_name = "Kurs"
        verbose_name_plural = "Kursy"
    def __str__(self):
        return self.nazwa

class Lekcja(models.Model):
    tytul = models.CharField(max_length=100)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE, related_name='lekcje')
    autorzy = models.ManyToManyField(Autor, related_name='lekcje')
    class Meta:
        verbose_name = "Lekcja"
        verbose_name_plural = "Lekcje"
    def __str__(self):
        return self.tytul