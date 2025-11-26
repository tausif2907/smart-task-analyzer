from django.urls import path
from . import views
urlpatterns = [
    path('tasks/analyze/', views.analyze),
    path('tasks/suggest/', views.suggest),
]
