"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from classiscoming import views

from classiscoming.views import obter_eventos_usuario
from classiscoming.views import obter_participantes_evento

router = routers.DefaultRouter(schema_title='Pastebin API')
router.register(r'instituicao', views.InstituicaoViewSet)
router.register(r'curso', views.CursoViewSet)
router.register(r'tipoevento', views.TipoEventoViewSet)
router.register(r'evento', views.EventoViewSet)
router.register(r'tipousuario', views.TipoUsuarioViewSet)
router.register(r'usuario', views.UsuarioViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^eventosusuario/(?P<usuario>[0-9]+)$', obter_eventos_usuario),
    url(r'^participantesevento/(?P<evento>[0-9]+)$', obter_participantes_evento),
]
