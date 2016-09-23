from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class PostsConfig(ModuleMixin, AppConfig):
    name = 'posts'
    icon = '<i class="material-icons">crop_din</i>'