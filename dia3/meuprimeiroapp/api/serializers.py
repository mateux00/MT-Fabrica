from rest_framework.serializers import ModelSerializer
from ..models import PessoBancoDeDados

class PessoaSerialazer(ModelSerializer):
        class Meta:
                model = PessoBancoDeDados
                fields = ['id', 'primeiro_nome','segundo_nome', 'idade']