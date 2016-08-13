from django.contrib import admin
from .models import Instituicao #admin
from .models import Curso 
from .models import InstituicaoCurso
from .models import TipoEvento
from .models import Evento
from .models import CursoEvento
from .models import OcorrenciaEvento
from .models import TipoUsuario
from .models import Usuario      
from .models import UsuarioInstituicao
from .models import UsuarioEvento
from .models import FaltaOcorrenciaEvento

# Register your models here.
admin.site.register(Instituicao)
admin.site.register(Curso)
admin.site.register(InstituicaoCurso)
admin.site.register(TipoEvento)
admin.site.register(Evento)
admin.site.register(CursoEvento)
admin.site.register(OcorrenciaEvento)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(UsuarioInstituicao)
admin.site.register(UsuarioEvento)
admin.site.register(FaltaOcorrenciaEvento)