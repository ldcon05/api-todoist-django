from django.urls import path

from . import views

urlpatterns = [
    path('', views.notes, name='index'),
    path('<int:id>', views.note_detail)
]