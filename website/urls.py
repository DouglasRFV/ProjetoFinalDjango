from django.urls import include, re_path, path
from .views import (
    home, 
)    

urlpatterns = [
    re_path(r'^$', home, name='website_home'),

]
