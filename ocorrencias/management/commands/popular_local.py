from django.core.management.base import BaseCommand
from ocorrencias.models import LocalObito

class Command(BaseCommand):
    help = 'Popula a tabela localobito com os valores padrão'

    def handle(self, *args, **kwargs):
        opcoes = ['NO LOCAL', 'HOSPITAL']
        adicionados = 0

        for descricao in opcoes:
            obj, criado = LocalObito.objects.get_or_create(descricao=descricao)
            if criado:
                adicionados += 1

        self.stdout.write(self.style.SUCCESS(f'{adicionados} registros adicionados com sucesso à tabela TraficoPosse.'))
