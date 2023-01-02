from django.urls import path
from . import views

urlpatterns = [
    path("matriculas/", views.MatriculaView.as_view()),
    path("aluno/<int:pk>/matriculas/", views.ListaMatriculasAluno.as_view()),
    path("curso/<int:pk>/matriculas/", views.ListaAlunosMatriculados.as_view()),
]
