
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Ocorrencia, SituacaoCarceraria,LocalObito,Tipo, Cidade, Orcrim, CausaFato, MeioEmpregado, Sexo, FaixaEtaria, Mes, Intervalo,DiaSemana, CorPele, TráficoPosse, Turno
from .forms import OcorrenciaForm, TipoForm, CidadeForm, OrcrimForm, CausaFatoForm, MeioEmpregadoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
import pandas as pd
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário cadastrado com sucesso!')
            return redirect('login')  # ou 'ocorrencia_list'
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



#IMPORTAR DADOS
class ImportarDadosView(LoginRequiredMixin, View):
    template_name = 'ocorrencias/importar_dados.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            excel_file = request.FILES['arquivo']
            df = pd.read_excel(excel_file)

            for _, row in df.iterrows():
                # Chaves estrangeiras com get_or_create
                faixa_etaria = FaixaEtaria.objects.get_or_create(descricao=row['Faixa etária'])[0]
                sexo = Sexo.objects.get_or_create(nome=row['Sexo'])[0]
                cidade = Cidade.objects.get_or_create(nome=row['Cidade'])[0]
                mes = Mes.objects.get_or_create(nome=row['Mês'])[0]
                intervalo = Intervalo.objects.get_or_create(descricao=row['Intervalo'])[0]
                turno = Turno.objects.get_or_create(descricao=row['Turno'])[0]
                dia_semana = DiaSemana.objects.get_or_create(descricao=row['Dia da semana'])[0]
                tipo = Tipo.objects.get_or_create(nome=row['Tipo'])[0]
                cor_pele = CorPele.objects.get_or_create(descricao=row['Cor de pele'])[0]
                causa_fato = CausaFato.objects.get_or_create(descricao=row['Causa do fato'])[0]
                trafico_posse = TráficoPosse.objects.get_or_create(descricao=row['Tráfico/Posse'])[0]
                orcrim = Orcrim.objects.get_or_create(descricao=row['ORCRIM'])[0]
                meio_empregado = MeioEmpregado.objects.get_or_create(descricao=row['Meio empregado'])[0]
                local_obito = LocalObito.objects.get_or_create(descricao=row['Local do óbito'])[0]
                situacao_carceraria = SituacaoCarceraria.objects.get_or_create(descricao=row['Situação carcerária'])[0]

                # Conversão da hora
                hora_valor = pd.to_datetime(row['Hora'], errors='coerce')
                hora = hora_valor.time() if pd.notna(hora_valor) else None

                # Tratamento de possíveis NaNs para campos numéricos
                ano = int(row['ANO']) if pd.notna(row['ANO']) else 0
                idade = int(row['Idade']) if pd.notna(row['Idade']) else 0
                ano_registro = int(row['Ano Registro']) if pd.notna(row['Ano Registro']) else 0
                numero_registro = int(row['Número Inteiro Ocorrência']) if pd.notna(row['Número Inteiro Ocorrência']) else 0

                ocorrencia = Ocorrencia(
                    ano=ano,
                    nome=row['Nome'],
                    idade=idade,
                    faixa_etaria=faixa_etaria,
                    profissao=row['Profissão'],
                    sexo=sexo,
                    documento=row['Documento'],
                    endereco_fato=row['Endereço do fato'],
                    numero=row['NR'],
                    bairro=row['Bairro'],
                    cidade=cidade,
                    opm=row['OPM'],
                    data_fato=pd.to_datetime(row['Data do fato'], errors='coerce'),
                    mes=mes,
                    hora=hora,
                    intervalo=intervalo,
                    turno=turno,
                    dia_semana=dia_semana,
                    tipo=tipo,
                    local_obito=local_obito,
                    cor_pele=cor_pele,
                    possui_antecedentes=row['Possui antecedentes criminais'],
                    situacao_carceraria=situacao_carceraria,
                    causa_fato=causa_fato,
                    trafico_posse=trafico_posse,
                    orcrim=orcrim,
                    coordenadas_geograficas=row['Coordenadas'],
                    latitude=row['Latitude'],
                    longitude=row['Longitude'],
                    historico=row['Histórico'],
                    orgao_registro=row['Órgão Registro'],
                    ano_registro=ano_registro,
                    numero_registro=numero_registro,
                    meio_empregado=meio_empregado,
                    nome_autor=row['Nome do autor(a)'],
                    rg_autor=row['RG do Autor(a)'],
                )

                ocorrencia.save()

            messages.success(request, "Importação realizada com sucesso.")
        except Exception as e:
            messages.error(request, f"Erro na importação: {e}")

        return redirect('importar_dados')

#EXPORTAR DADOS
class ExportarDadosView(LoginRequiredMixin,View):
    def get(self, request):
        ocorrencias = Ocorrencia.objects.select_related(
            'faixa_etaria', 'sexo', 'cidade', 'mes', 'intervalo',
            'turno', 'dia_semana', 'tipo', 'local_obito', 'cor_pele',
            'situacao_carceraria', 'causa_fato', 'trafico_posse', 'orcrim',
            'meio_empregado'
        )

        data = []
        for o in ocorrencias:
            data.append({
                'ANO': o.ano,
                'Nome': o.nome,
                'Idade': o.idade,
                'Faixa etária': o.faixa_etaria.descricao if o.faixa_etaria else '',
                'Profissão': o.profissao,
                'Sexo': o.sexo.nome if o.sexo else '',
                'Documento': o.documento,
                'Endereço do fato': o.endereco_fato,
                'NR': o.numero,
                'Bairro': o.bairro,
                'Cidade': o.cidade.nome if o.cidade else '',
                'OPM': o.opm,
                'Data do fato': o.data_fato,
                'Mês': o.mes.nome if o.mes else '',
                'Hora': o.hora,
                'Intervalo': o.intervalo.descricao if o.intervalo else '',
                'Turno': o.turno.descricao if o.turno else '',
                'Dia da semana': o.dia_semana.descricao if o.dia_semana else '',
                'Tipo': o.tipo.nome if o.tipo else '',
                'Local do óbito': o.local_obito.descricao if o.local_obito else '',
                'Cor de pele': o.cor_pele.descricao if o.cor_pele else '',
                'Possui antecedentes criminais': o.possui_antecedentes,
                'Situação carcerária': o.situacao_carceraria.descricao if o.situacao_carceraria else '',
                'Causa do fato': o.causa_fato.descricao if o.causa_fato else '',
                'Tráfico/Posse': o.trafico_posse.descricao if o.trafico_posse else '',
                'ORCRIM': o.orcrim.descricao if o.orcrim else '',
                'Coordenadas': o.coordenadas_geograficas,
                'Latitude': o.latitude,
                'Longitude': o.longitude,
                'Histórico': o.historico,
                'Órgão Registro': o.orgao_registro,
                'Ano Registro': o.ano_registro,
                'Número Inteiro Ocorrência': o.numero_registro,
                'Meio empregado': o.meio_empregado.descricao if o.meio_empregado else '',
                'Nome do autor(a)': o.nome_autor,
                'RG do Autor(a)': o.rg_autor,
            })

        df = pd.DataFrame(data)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=ocorrencias_exportadas.xlsx'
        df.to_excel(response, index=False)

        return response

# Ocorrências
class OcorrenciaListView(LoginRequiredMixin,ListView):
    model = Ocorrencia
    template_name = 'ocorrencias/ocorrencia_list.html'
    context_object_name = 'ocorrencias'
    paginate_by = 10
    ordering = ['-id']

class OcorrenciaCreateView(LoginRequiredMixin,CreateView):
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencias/ocorrencia_form.html'
    success_url = reverse_lazy('ocorrencia_list')

class OcorrenciaUpdateView(LoginRequiredMixin,UpdateView):
    model = Ocorrencia
    form_class = OcorrenciaForm
    template_name = 'ocorrencias/ocorrencia_form.html'
    success_url = reverse_lazy('ocorrencia_list')

class OcorrenciaDeleteView(LoginRequiredMixin,DeleteView):
    model = Ocorrencia
    template_name = 'ocorrencias/ocorrencia_confirm_delete.html'
    success_url = reverse_lazy('ocorrencia_list')

class OcorrenciaDetailView(LoginRequiredMixin,DetailView):
    model = Ocorrencia
    template_name = 'ocorrencias/ocorrencia_detail.html'
    context_object_name = 'ocorrencia'


# Tipos
class TipoListView(LoginRequiredMixin,ListView):
    model = Tipo
    template_name = 'ocorrencias/tipo_list.html'
    context_object_name = 'tipos'

class TipoCreateView(LoginRequiredMixin,CreateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'ocorrencias/tipo_form.html'
    success_url = reverse_lazy('tipo_list')

class TipoUpdateView(LoginRequiredMixin,UpdateView):
    model = Tipo
    form_class = TipoForm
    template_name = 'ocorrencias/tipo_form.html'
    success_url = reverse_lazy('tipo_list')

class TipoDeleteView(LoginRequiredMixin,DeleteView):
    model = Tipo
    template_name = 'ocorrencias/tipo_confirm_delete.html'
    success_url = reverse_lazy('tipo_list')


# Cidades
class CidadeListView(LoginRequiredMixin,ListView):
    model = Cidade
    template_name = 'ocorrencias/cidade_list.html'
    context_object_name = 'cidades'

class CidadeCreateView(LoginRequiredMixin,CreateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'ocorrencias/cidade_form.html'
    success_url = reverse_lazy('cidade_list')

class CidadeUpdateView(LoginRequiredMixin,UpdateView):
    model = Cidade
    form_class = CidadeForm
    template_name = 'ocorrencias/cidade_form.html'
    success_url = reverse_lazy('cidade_list')

class CidadeDeleteView(LoginRequiredMixin,DeleteView):
    model = Cidade
    template_name = 'ocorrencias/cidade_confirm_delete.html'
    success_url = reverse_lazy('cidade_list')
    
#ORCRIM    
class OrcrimListView(LoginRequiredMixin,ListView):
    model = Orcrim
    template_name = 'ocorrencias/orcrim_list.html'
    context_object_name = 'orcrims'

class OrcrimCreateView(LoginRequiredMixin,CreateView):
    model = Orcrim
    form_class = OrcrimForm
    template_name = 'ocorrencias/orcrim_form.html'
    success_url = reverse_lazy('orcrim_list')

class OrcrimUpdateView(LoginRequiredMixin,UpdateView):
    model = Orcrim
    form_class = OrcrimForm
    template_name = 'ocorrencias/orcrim_form.html'
    success_url = reverse_lazy('orcrim_list')

class OrcrimDeleteView(LoginRequiredMixin,DeleteView):
    model = Orcrim
    template_name = 'ocorrencias/orcrim_confirm_delete.html'
    success_url = reverse_lazy('orcrim_list')
    
#CAUSA DO FATO
class CausaFatoListView(LoginRequiredMixin,ListView):
    model = CausaFato
    template_name = 'ocorrencias/causafato_list.html'
    context_object_name = 'causas'

class CausaFatoCreateView(LoginRequiredMixin,CreateView):
    model = CausaFato
    fields = ['descricao']
    template_name = 'ocorrencias/causafato_form.html'
    success_url = reverse_lazy('causafato_list')

class CausaFatoUpdateView(LoginRequiredMixin,UpdateView):
    model = CausaFato
    fields = ['descricao']
    template_name = 'ocorrencias/causafato_form.html'
    success_url = reverse_lazy('causafato_list')

class CausaFatoDeleteView(LoginRequiredMixin,DeleteView):
    model = CausaFato
    template_name = 'ocorrencias/causafato_confirm_delete.html'
    success_url = reverse_lazy('causafato_list')
    
#MEIO EMPREGADO
class MeioEmpregadoListView(LoginRequiredMixin,ListView):
    model = MeioEmpregado
    template_name = 'ocorrencias/meioempregado_list.html'
    context_object_name = 'meios'

class MeioEmpregadoCreateView(LoginRequiredMixin,CreateView):
    model = MeioEmpregado
    form_class = MeioEmpregadoForm
    template_name = 'ocorrencias/meioempregado_form.html'
    success_url = reverse_lazy('meioempregado_list')

class MeioEmpregadoUpdateView(LoginRequiredMixin,UpdateView):
    model = MeioEmpregado
    form_class = MeioEmpregadoForm
    template_name = 'ocorrencias/meioempregado_form.html'
    success_url = reverse_lazy('meioempregado_list')

class MeioEmpregadoDeleteView(LoginRequiredMixin,DeleteView):
    model = MeioEmpregado
    template_name = 'ocorrencias/meioempregado_confirm_delete.html'
    success_url = reverse_lazy('meioempregado_list')