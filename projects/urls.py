from django.urls import path
from projects.views import *

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),  # страница проекта
    path('create-project/', createProject, name='create-project'),  # страница создания проекта
    path('update-project/<str:pk>/', updateProject, name='update-project'),  # страница обновления проекта
    path('delete-project/<str:pk>/', deleteProject, name='delete-project'),  # страница удаления проекта
]