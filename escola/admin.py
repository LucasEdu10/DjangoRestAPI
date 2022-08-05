from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

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

class MatriculasAdmin(admin.ModelAdmin):
    list_display = ('id','aluno', 'curso', 'periodo')
    list_display_links = ('id',)

admin.site.register(Aluno, AlunosAdmin)
admin.site.register(Curso, CursosAdmin)
admin.site.register(Matricula, MatriculasAdmin)
# Register your models here.
