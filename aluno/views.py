from .models import Aluno
from .serializers import AlunoSerializer
from rest_framework import generics


class AlunoView(generics.ListCreateAPIView):
    """Exibindo todos os cursos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
