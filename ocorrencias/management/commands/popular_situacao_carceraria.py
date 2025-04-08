from django.core.management.base import BaseCommand
from ocorrencias.models import SituacaoCarceraria

class Command(BaseCommand):
    help = 'Popula a tabela SituacaoCarcerária com os campos padrão'

    def handle(self, *args, **kwargs):
        situacao_carceraria = ['EX-DETENTO','DETENTO','MONITORADO', 'FORAGIDO', 'EX-CASE', 'PRISÃO DOMICILIAR', 'PROCURADO', 'NÃO POSSUI', 'PREJUDICADO']
        adicionados = 0

        for desc in situacao_carceraria:
            obj, criado = SituacaoCarceraria.objects.get_or_create(descricao=desc)
            if criado:
                adicionados += 1

        self.stdout.write(self.style.SUCCESS(
            f'{adicionados} campos adicionados com sucesso.'
        ))
