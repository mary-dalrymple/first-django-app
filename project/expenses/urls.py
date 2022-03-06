from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # example: /summary/1/
  path('summary/<int:summary_id>/', views.summary, name='summary'),
]
