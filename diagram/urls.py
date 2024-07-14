from django.urls import path
from . import views

urlpatterns = [
    path("", views.DiagramView.as_view(), name='index'),
]
