from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.editor, name='editor'),
    path('admin/', admin.site.urls)
]
