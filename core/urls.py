from django.urls import include, re_path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos, 
    lista_movRotativos,
    lista_mensalistas,
    lista_movMensalistas,
    pessoa_novo,
    veiculo_novo,
    movRotativo_novo,
    mensalista_novo,
    movMensalistas_novo
)    

urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),

    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),

    re_path(r'^movRotativos/$', lista_movRotativos, name='core_lista_movRotativos'),
    re_path(r'^movRotativo-novo/$', movRotativo_novo, name='core_movRotativo_novo'),

    re_path(r'^mensalista/$', lista_mensalistas, name='core_lista_mensalista'),
    re_path(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),

    re_path(r'^movMensalistas/$', lista_movMensalistas, name='core_lista_movMensalistas'),
    re_path(r'^movMensalista-novo/$', movMensalistas_novo, name='core_movMensalista_novo'),
]
