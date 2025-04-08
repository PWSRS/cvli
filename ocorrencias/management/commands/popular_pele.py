from django.core.management.base import BaseCommand
from ocorrencias.models import CorPele

class Command(BaseCommand):
    help = 'Popula a tabela CorPele com cores padrão'

    def handle(self, *args, **kwargs):
        cores = ['Branca', 'Parda', 'Negra', 'Amarela', 'Indígena', 'Não Informado']
        adicionados = 0

        for desc in cores:
            obj, criado = CorPele.objects.get_or_create(descricao=desc)
            if criado:
                adicionados += 1

        self.stdout.write(self.style.SUCCESS(
            f'{adicionados} cores de pele adicionadas com sucesso.'
        ))
