from django.urls import path
from api.views import *

urlpatterns = [
    path('', getRoutes),
    path('projects/', getProjects),
    path('projects/<str:pk>/', getProject),
]