from django import forms
from .models import (
    Ocorrencia,
    Cidade,
    Tipo,
    Sexo,
    FaixaEtaria,
    Turno,
    Intervalo,
    DiaSemana,
    LocalObito,
    CorPele,
    SituacaoCarceraria,
    CausaFato,
    TráficoPosse,
    Orcrim,
    MeioEmpregado
)


class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = '__all__'
        widgets = {
            'data_fato': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class CidadeForm(forms.ModelForm):
    class Meta:
        model = Cidade
        fields = ['nome']


class TipoForm(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = ['nome']


class SexoForm(forms.ModelForm):
    class Meta:
        model = Sexo
        fields = ['nome']


class FaixaEtariaForm(forms.ModelForm):
    class Meta:
        model = FaixaEtaria
        fields = ['descricao']


class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['descricao']


class IntervaloForm(forms.ModelForm):
    class Meta:
        model = Intervalo
        fields = ['descricao']


class DiaSemanaForm(forms.ModelForm):
    class Meta:
        model = DiaSemana
        fields = ['descricao']


class LocalObitoForm(forms.ModelForm):
    class Meta:
        model = LocalObito
        fields = ['descricao']


class CorPeleForm(forms.ModelForm):
    class Meta:
        model = CorPele
        fields = ['descricao']


class SituacaoCarcerariaForm(forms.ModelForm):
    class Meta:
        model = SituacaoCarceraria
        fields = ['descricao']


class CausaFatoForm(forms.ModelForm):
    class Meta:
        model = CausaFato
        fields = ['descricao']


class TraficoPosseForm(forms.ModelForm):
    class Meta:
        model = TráficoPosse
        fields = ['descricao']


class OrcrimForm(forms.ModelForm):
    class Meta:
        model = Orcrim
        fields = ['descricao']


class MeioEmpregadoForm(forms.ModelForm):
    class Meta:
        model = MeioEmpregado
        fields = ['descricao']
