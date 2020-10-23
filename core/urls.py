from django.urls import include, re_path
from .views import (
    home, 
    lista_pessoas, 
    pessoa_novo,
    pessoa_update,
    pessoa_delete,

    lista_veiculos, 
    veiculo_novo,
    veiculo_update,
    veiculo_delete,
    
    lista_movRotativos,
    movRotativo_novo,
    movRotativo_update,
    movRotativo_delete,
    
    lista_mensalistas,
    mensalista_novo,
    mensalista_update,
    mensalista_delete,
    
    lista_movMensalistas,
    movMensalistas_novo,
    movMensalista_update,
    movMensalista_delete,
)    

urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'^pessoas/$', lista_pessoas, name='core_lista_pessoas'),
    re_path(r'^pessoa-novo/$', pessoa_novo, name='core_pessoa_novo'),
    re_path(r'^pessoa-update/(?P<id>\d+)/$', pessoa_update, name='core_pessoa_update'),
    re_path(r'^pessoa-delete/(?P<id>\d+)/$', pessoa_delete, name='core_pessoa_delete'),

    re_path(r'^veiculos/$', lista_veiculos, name='core_lista_veiculos'),
    re_path(r'^veiculo-novo/$', veiculo_novo, name='core_veiculo_novo'),
    re_path(r'^veiculo-update/(?P<id>\d+)/$', veiculo_update, name='core_veiculo_update'),
    re_path(r'^veiculo-delete/(?P<id>\d+)/$', veiculo_delete, name='core_veiculo_delete'),

    re_path(r'^movRotativos/$', lista_movRotativos, name='core_lista_movRotativos'),
    re_path(r'^movRotativo-novo/$', movRotativo_novo, name='core_movRotativo_novo'),
    re_path(r'^movRotativo-update/(?P<id>\d+)/$', movRotativo_update, name='core_movRotativo_update'),
    re_path(r'^movRotativo-delete/(?P<id>\d+)/$', movRotativo_delete, name='core_movRotativo_delete'),

    re_path(r'^mensalista/$', lista_mensalistas, name='core_lista_mensalistas'),
    re_path(r'^mensalista-novo/$', mensalista_novo, name='core_mensalista_novo'),
    re_path(r'^mensalista-update/(?P<id>\d+)/$', mensalista_update, name='core_mensalista_update'),
    re_path(r'^mensalista-delete/(?P<id>\d+)/$', mensalista_delete, name='core_mensalista_delete'),

    re_path(r'^movMensalistas/$', lista_movMensalistas, name='core_lista_movMensalistas'),
    re_path(r'^movMensalista-novo/$', movMensalistas_novo, name='core_movMensalista_novo'),
    re_path(r'^movMensalista-update/(?P<id>\d+)/$', movMensalista_update, name='core_movMensalista_update'),
    re_path(r'^movMensalista-delete/(?P<id>\d+)/$', movMensalista_delete, name='core_movMensalista_delete'),

]
