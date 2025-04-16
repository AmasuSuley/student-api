from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students_view),
    path('subjects/', views.subjects_view),
]
