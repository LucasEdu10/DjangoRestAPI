from django.contrib import admin
from escola.models import Aluno, Curso

class AlunosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'dt_nascimento')
    list_display_links = ('id', 'nome')
    search_fields = ('nome',)
    list_per_page = 20


class CursosAdmin(admin.ModelAdmin):
    list_display = ('id','codigo_curso', 'descricao', 'nivel')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)
    list_per_page = 20

admin.site.register(Aluno, AlunosAdmin)
admin.site.register(Curso, CursosAdmin)
# Register your models here.
