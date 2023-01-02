from django.contrib import admin

from matricula.models import Matricula


class Matriculas(admin.ModelAdmin):
    list_display = ['id', 'aluno', 'curso', 'periodo']
    list_display_links = ['id']

admin.site.register(Matricula, Matriculas)