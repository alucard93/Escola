from .models import Matricula
from .serializers import MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculados
from rest_framework import generics


class MatriculaView(generics.ListCreateAPIView):
    """Exibindo todos os cursos"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset

    serializer_class = ListaMatriculaAlunoSerializer


class ListaAlunosMatriculados(generics.ListAPIView):
    """Listando alunos e alunas matriculados em um curso"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset

    serializer_class = ListaAlunosMatriculados