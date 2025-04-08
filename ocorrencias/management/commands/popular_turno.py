from django.core.management.base import BaseCommand
from ocorrencias.models import Turno

class Command(BaseCommand):
    help = 'Popula a tabela Turno com os turnos padrão'

    def handle(self, *args, **kwargs):
        turnos = ['1º', '2º', '3º', '4º']
        adicionados = 0

        for desc in turnos:
            obj, criado = Turno.objects.get_or_create(descricao=desc)
            if criado:
                adicionados += 1

        self.stdout.write(self.style.SUCCESS(
            f'{adicionados} turnos adicionados com sucesso.'
        ))
