from django.contrib import admin

from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "categoria", "publicada")
    list_display_links = ("id", "nome")
    search_fields = ("nome",)
    list_filter = ("categoria","user_id",)
    list_per_page = 10
    list_editable = ("publicada",)

admin.site.register(Fotografia, ListandoFotografias)
