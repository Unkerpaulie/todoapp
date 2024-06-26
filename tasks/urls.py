from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('done/', views.done, name="done"),
    path('undone/', views.undone, name="undone"),
    path('<int:pk>/detail/', views.detail, name="detail"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk>/delete/', views.delete, name="delete"),
]
