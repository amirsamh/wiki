from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("result", views.result, name="result"),
    path("new", views.new, name="new"),
    path("random", views.random, name="random"),
    path("edit", views.edit, name="edit"),
    path("show_edit", views.show_edit, name="show_edit"),
    path("<str:title>", views.entry, name="entry")
]
