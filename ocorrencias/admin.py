from django.contrib import admin
from .models import Ocorrencia, Tipo, SituacaoCarceraria

admin.site.register(Ocorrencia)
admin.site.register(Tipo)
admin.site.register(SituacaoCarceraria)