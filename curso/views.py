from .models import Curso
from .serializers import CursoSerializer
from rest_framework import generics


class CursoView(generics.ListCreateAPIView):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
