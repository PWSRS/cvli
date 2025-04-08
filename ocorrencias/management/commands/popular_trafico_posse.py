from django.core.management.base import BaseCommand
from ocorrencias.models import TráficoPosse

class Command(BaseCommand):
    help = 'Popula a tabela TraficoPosse com os valores padrão'

    def handle(self, *args, **kwargs):
        opcoes = ['POSSE', 'TRÁFICO', 'NÃO POSSUI', 'PREJUDICADO']
        adicionados = 0

        for descricao in opcoes:
            obj, criado = TráficoPosse.objects.get_or_create(descricao=descricao)
            if criado:
                adicionados += 1

        self.stdout.write(self.style.SUCCESS(f'{adicionados} registros adicionados com sucesso à tabela TraficoPosse.'))
