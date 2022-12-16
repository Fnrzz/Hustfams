from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project',views.project,name='project')
]