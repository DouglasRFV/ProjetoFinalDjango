from django.urls import include, re_path, path
from .views import (
    home, 
    contato,
    servicos,
    sobre,
    planos
)    

urlpatterns = [
    re_path(r'^$', home, name='website_home'),
    re_path(r'^contato$', contato, name='website_contato'),
    re_path(r'^servicos$', servicos, name='website_servicos'),
    re_path(r'^sobre$', sobre, name='website_sobre'),
    re_path(r'^planos$', planos, name='website_planos'),

]
