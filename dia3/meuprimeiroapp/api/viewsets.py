from rest_framework.viewsets import ModelViewSet
from .serializers import PessoaSerialazer
from ..models import PessoBancoDeDados


class PesossaViewSet(ModelViewSet):
    serializer_class = PessoaSerialazer
    queryset = PessoBancoDeDados.objects.all()
