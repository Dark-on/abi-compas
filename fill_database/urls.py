from django.urls import path

from . import views


urlpatterns = [
    path('', views.update_tables, name='update_tables')
]