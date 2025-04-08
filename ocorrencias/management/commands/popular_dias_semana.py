from django.core.management.base import BaseCommand
from ocorrencias.models import DiaSemana

class Command(BaseCommand):
    help = 'Popula a tabela DiaSemana com os dias da semana'

    def handle(self, *args, **kwargs):
        dias = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']

        adicionados = 0
        for nome in dias:
            obj, criado = DiaSemana.objects.get_or_create(descricao=nome)  # aqui!
            if criado:
                adicionados += 1

        self.stdout.write(self.style.SUCCESS(
            f'{adicionados} dias da semana adicionados com sucesso.'
        ))
