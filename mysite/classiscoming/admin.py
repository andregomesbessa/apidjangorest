from django.contrib import admin
from .models import Instituicao #admin
from .models import Curso 
from .models import Disciplina
from .models import Aula
from .models import Perfil
from .models import Usuario      

# Register your models here.
admin.site.register(Instituicao)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Aula)
admin.site.register(Perfil)
admin.site.register(Usuario)