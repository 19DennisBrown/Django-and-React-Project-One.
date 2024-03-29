
from django.urls import path
from . import views



urlpatterns = [
  path('students/', views.Students_view, name='students'),
  path('student/<int:id>/', views.Student_view, name='student'),
]