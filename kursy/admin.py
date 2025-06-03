from django.contrib import admin
from kursy.models import Kurs, Lekcja, Autor

class KursAdmin(admin.ModelAdmin):
    list_display = ('nazwa', 'typ', 'autor')

admin.site.register(Kurs, KursAdmin)
admin.site.register(Lekcja)
admin.site.register(Autor)
