from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Pais, Estado, Cidade, Empresa, EstadoCivil, Escolaridade
from .forms import PaisForm, EstadoForm, CidadeForm, EmpresaForm, EstadoCivilForm, EscolaridadeForm
from .forms_extra import ObjetivoForm, BeneficioINSSForm
from .search_forms import PaisSearchForm, EstadoSearchForm, CidadeSearchForm
from .models import Objetivo, BeneficioINSS

# Views para Objetivo
@login_required
def objetivos(request):
    objetivos_list = Objetivo.objects.all()
    
# Views para BeneficioINSS
@login_required
def beneficios_inss(request):
    beneficios_list = BeneficioINSS.objects.all()
    paginator = Paginator(beneficios_list, 10)
    page_number = request.GET.get('page')
    beneficios = paginator.get_page(page_number)
    context = {
        'page_title': 'Benefícios INSS',
        'beneficios': beneficios,
    }
    return render(request, 'dashboard/basico/beneficios_inss.html', context)

@login_required
def beneficio_inss_create(request):
    if request.method == 'POST':
        form = BeneficioINSSForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Benefício INSS criado com sucesso!')
            return redirect('dashboard:beneficios_inss')
        else:
            messages.error(request, 'Erro ao criar o benefício.')
    else:
        form = BeneficioINSSForm()
    return render(request, 'dashboard/basico/beneficios_inss_form.html', {'form': form, 'page_title': 'Novo Benefício INSS'})

@login_required
def beneficio_inss_update(request, pk):
    beneficio = get_object_or_404(BeneficioINSS, pk=pk)
    if request.method == 'POST':
        form = BeneficioINSSForm(request.POST, instance=beneficio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Benefício INSS atualizado com sucesso!')
            return redirect('dashboard:beneficios_inss')
        else:
            messages.error(request, 'Erro ao atualizar o benefício.')
    else:
        form = BeneficioINSSForm(instance=beneficio)
    return render(request, 'dashboard/basico/beneficios_inss_form.html', {'form': form, 'page_title': 'Editar Benefício INSS'})

@login_required
def beneficio_inss_delete(request, pk):
    beneficio = get_object_or_404(BeneficioINSS, pk=pk)
    if request.method == 'POST':
        try:
            beneficio.delete()
            messages.success(request, 'Benefício INSS removido com sucesso!')
            return redirect('dashboard:beneficios_inss')
        except Exception as e:
            messages.error(request, f'Erro ao deletar benefício: {e}')
    return render(request, 'dashboard/basico/beneficios_inss_confirm_delete.html', {'object': beneficio, 'page_title': 'Excluir Benefício INSS'})
    paginator = Paginator(objetivos_list, 10)
    page_number = request.GET.get('page')
    objetivos = paginator.get_page(page_number)
    context = {
        'page_title': 'Objetivos',
        'objetivos': objetivos,
    }
    return render(request, 'dashboard/basico/objetivos.html', context)

@login_required
def objetivo_create(request):
    if request.method == 'POST':
        form = ObjetivoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Objetivo criado com sucesso!')
            return redirect('dashboard:objetivos')
        else:
            messages.error(request, 'Erro ao criar o objetivo.')
    else:
        form = ObjetivoForm()
    return render(request, 'dashboard/basico/objetivos_form.html', {'form': form, 'page_title': 'Novo Objetivo'})

@login_required
def objetivo_update(request, pk):
    objetivo = get_object_or_404(Objetivo, pk=pk)
    if request.method == 'POST':
        form = ObjetivoForm(request.POST, instance=objetivo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Objetivo atualizado com sucesso!')
            return redirect('dashboard:objetivos')
        else:
            messages.error(request, 'Erro ao atualizar o objetivo.')
    else:
        form = ObjetivoForm(instance=objetivo)
    return render(request, 'dashboard/basico/objetivos_form.html', {'form': form, 'page_title': 'Editar Objetivo'})

@login_required
def objetivo_delete(request, pk):
    objetivo = get_object_or_404(Objetivo, pk=pk)
    if request.method == 'POST':
        try:
            objetivo.delete()
            messages.success(request, 'Objetivo removido com sucesso!')
            return redirect('dashboard:objetivos')
        except Exception as e:
            messages.error(request, f'Erro ao deletar objetivo: {e}')
    return render(request, 'dashboard/basico/objetivos_confirm_delete.html', {'object': objetivo, 'page_title': 'Excluir Objetivo'})

@login_required
def index(request):
    context = {
        'user_name': request.user.get_full_name() or request.user.username,
        'page_title': 'Dashboard'
    }
    return render(request, 'dashboard/index.html', context)

# Views para Estado Civil
@login_required
def estados_civis(request):
    estados_civis_list = EstadoCivil.objects.all()
    paginator = Paginator(estados_civis_list, 10)
    page_number = request.GET.get('page')
    estados_civis = paginator.get_page(page_number)
    context = {
        'page_title': 'Estados Civis',
        'estados_civis': estados_civis,
    }
    return render(request, 'dashboard/basico/estados_civis.html', context)

# Views para Escolaridade
@login_required
def escolaridades(request):
    escolaridades_list = Escolaridade.objects.all()
    paginator = Paginator(escolaridades_list, 10)
    page_number = request.GET.get('page')
    escolaridades = paginator.get_page(page_number)
    context = {
        'page_title': 'Escolaridades',
        'escolaridades': escolaridades,
    }
    return render(request, 'dashboard/basico/escolaridades.html', context)

@login_required
def escolaridade_create(request):
    if request.method == 'POST':
        form = EscolaridadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Escolaridade criada com sucesso!')
            return redirect('dashboard:escolaridades')
        else:
            messages.error(request, 'Erro ao criar a escolaridade.')
    else:
        form = EscolaridadeForm()
    return render(request, 'dashboard/basico/escolaridades_form.html', {'form': form, 'page_title': 'Nova Escolaridade'})

@login_required
def escolaridade_update(request, pk):
    escolaridade = get_object_or_404(Escolaridade, pk=pk)
    if request.method == 'POST':
        form = EscolaridadeForm(request.POST, instance=escolaridade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Escolaridade atualizada com sucesso!')
            return redirect('dashboard:escolaridades')
        else:
            messages.error(request, 'Erro ao atualizar a escolaridade.')
    else:
        form = EscolaridadeForm(instance=escolaridade)
    return render(request, 'dashboard/basico/escolaridades_form.html', {'form': form, 'page_title': 'Editar Escolaridade'})

@login_required
def escolaridade_delete(request, pk):
    escolaridade = get_object_or_404(Escolaridade, pk=pk)
    if request.method == 'POST':
        try:
            escolaridade.delete()
            messages.success(request, 'Escolaridade removida com sucesso!')
            return redirect('dashboard:escolaridades')
        except Exception as e:
            messages.error(request, f'Erro ao deletar escolaridade: {e}')
    return render(request, 'dashboard/basico/escolaridades_confirm_delete.html', {'object': escolaridade, 'page_title': 'Excluir Escolaridade'})

@login_required
def estado_civil_create(request):
    if request.method == 'POST':
        form = EstadoCivilForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estado Civil criado com sucesso!')
            return redirect('dashboard:estados_civis')
        else:
            messages.error(request, 'Erro ao criar o estado civil.')
    else:
        form = EstadoCivilForm()
    return render(request, 'dashboard/basico/estados_civis_form.html', {'form': form, 'page_title': 'Novo Estado Civil'})

@login_required
def estado_civil_update(request, pk):
    estado_civil = get_object_or_404(EstadoCivil, pk=pk)
    if request.method == 'POST':
        form = EstadoCivilForm(request.POST, instance=estado_civil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estado Civil atualizado com sucesso!')
            return redirect('dashboard:estados_civis')
        else:
            messages.error(request, 'Erro ao atualizar o estado civil.')
    else:
        form = EstadoCivilForm(instance=estado_civil)
    return render(request, 'dashboard/basico/estados_civis_form.html', {'form': form, 'page_title': 'Editar Estado Civil'})

@login_required
def estado_civil_delete(request, pk):
    estado_civil = get_object_or_404(EstadoCivil, pk=pk)
    if request.method == 'POST':
        try:
            estado_civil.delete()
            messages.success(request, 'Estado Civil removido com sucesso!')
            return redirect('dashboard:estados_civis')
        except Exception as e:
            messages.error(request, f'Erro ao deletar estado civil: {e}')
    return render(request, 'dashboard/basico/estados_civis_confirm_delete.html', {'object': estado_civil, 'page_title': 'Excluir Estado Civil'})

# Views para Empresa
@login_required
def empresas(request):
    empresas_list = Empresa.objects.all()
    paginator = Paginator(empresas_list, 10)
    page_number = request.GET.get('page')
    empresas = paginator.get_page(page_number)
    context = {
        'page_title': 'Empresas',
        'empresas': empresas,
    }
    return render(request, 'dashboard/empresa/empresas.html', context)

@login_required
def empresa_create(request):
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa criada com sucesso!')
            return redirect('dashboard:empresas')
        else:
            messages.error(request, 'Erro ao criar a empresa.')
    else:
        form = EmpresaForm()
    return render(request, 'dashboard/empresa/empresa_form.html', {'form': form, 'page_title': 'Nova Empresa'})

@login_required
def empresa_update(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa atualizada com sucesso!')
            return redirect('dashboard:empresas')
        else:
            messages.error(request, 'Erro ao atualizar a empresa.')
    else:
        form = EmpresaForm(instance=empresa)
    return render(request, 'dashboard/empresa/empresa_form.html', {'form': form, 'page_title': 'Editar Empresa'})

@login_required
def empresa_delete(request, pk):
    empresa = get_object_or_404(Empresa, pk=pk)
    if request.method == 'POST':
        try:
            empresa.delete()
            messages.success(request, 'Empresa removida com sucesso!')
            return redirect('dashboard:empresas')
        except Exception as e:
            messages.error(request, f'Erro ao deletar empresa: {e}')
    return render(request, 'dashboard/empresa/empresa_confirm_delete.html', {'object': empresa, 'page_title': 'Excluir Empresa'})


@login_required
def cadastros(request):
    context = {
        'page_title': 'Cadastros'
    }
    return render(request, 'dashboard/cadastros.html', context)

@login_required
def processos(request):
    context = {
        'page_title': 'Processos'
    }
    return render(request, 'dashboard/processos.html', context)

@login_required
def consultas(request):
    context = {
        'page_title': 'Consultas'
    }
    return render(request, 'dashboard/consultas.html', context)

@login_required
def relatorios(request):
    context = {
        'page_title': 'Relatórios'
    }
    return render(request, 'dashboard/relatorios.html', context)

@login_required
def configuracoes(request):
    context = {
        'page_title': 'Configurações'
    }
    return render(request, 'dashboard/configuracoes.html', context)

# Views para Países
@login_required
def paises(request):
    from .search_forms import PaisSearchForm
    search_form = PaisSearchForm(request.GET)
    paises_list = Pais.objects.all()

    if search_form.is_valid():
        if search_form.cleaned_data.get('nome'):
            paises_list = paises_list.filter(nome__icontains=search_form.cleaned_data['nome'])
        if search_form.cleaned_data.get('continente'):
            paises_list = paises_list.filter(continente__icontains=search_form.cleaned_data['continente'])

    paginator = Paginator(paises_list, 10)  # 10 países por página
    page_number = request.GET.get('page')
    paises = paginator.get_page(page_number)

    context = {
        'page_title': 'Países',
        'paises': paises,
        'search_form': search_form,
    }
    return render(request, 'dashboard/basico/paises_v2.html', context)

@login_required
def paises_create(request):
    if request.method == 'POST':
        form = PaisForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'País criado com sucesso!')
            return redirect('dashboard:paises')
        else:
            messages.error(request, 'Erro ao criar o país.')
    else:
        form = PaisForm()
    return render(request, 'dashboard/basico/paises_form.html', {'form': form, 'page_title': 'Novo País'})

@login_required
def paises_update(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        form = PaisForm(request.POST, instance=pais)
        if form.is_valid():
            form.save()
            messages.success(request, 'País atualizado com sucesso!')
            return redirect('dashboard:paises')
        else:
            messages.error(request, 'Erro ao atualizar o país.')
    else:
        form = PaisForm(instance=pais)
    return render(request, 'dashboard/basico/paises_form.html', {'form': form, 'page_title': 'Editar País'})

@login_required
def paises_delete(request, pk):
    pais = get_object_or_404(Pais, pk=pk)
    if request.method == 'POST':
        try:
            pais.delete()
            messages.success(request, 'País removido com sucesso!')
            return redirect('dashboard:paises')
        except Exception as e:
            messages.error(request, f'Erro ao deletar país: {e}')
    return render(request, 'dashboard/basico/paises_confirm_delete.html', {'object': pais, 'page_title': 'Excluir País'})

# Views para Estados
@login_required
def estados(request):
    from .search_forms import EstadoSearchForm
    search_form = EstadoSearchForm(request.GET)
    estados_list = Estado.objects.select_related('pais').all()

    if search_form.is_valid():
        if search_form.cleaned_data.get('nome'):
            estados_list = estados_list.filter(nome__icontains=search_form.cleaned_data['nome'])
        if search_form.cleaned_data.get('sigla'):
            estados_list = estados_list.filter(sigla__icontains=search_form.cleaned_data['sigla'])
        if search_form.cleaned_data.get('regiao'):
            estados_list = estados_list.filter(regiao__icontains=search_form.cleaned_data['regiao'])

    paginator = Paginator(estados_list, 10)  # 10 estados por página
    page_number = request.GET.get('page')
    estados = paginator.get_page(page_number)

    context = {
        'page_title': 'Estados',
        'estados': estados,
        'search_form': search_form,
    }
    return render(request, 'dashboard/basico/estados.html', context)

@login_required
def estados_create(request):
    if request.method == 'POST':
        form = EstadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estado criado com sucesso!')
            return redirect('dashboard:estados')
        else:
            messages.error(request, 'Erro ao criar o estado.')
    else:
        form = EstadoForm()
    return render(request, 'dashboard/basico/estados_form.html', {'form': form, 'page_title': 'Novo Estado'})

@login_required
def estados_update(request, pk):
    estado = get_object_or_404(Estado, pk=pk)
    if request.method == 'POST':
        form = EstadoForm(request.POST, instance=estado)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estado atualizado com sucesso!')
            return redirect('dashboard:estados')
        else:
            messages.error(request, 'Erro ao atualizar o estado.')
    else:
        form = EstadoForm(instance=estado)
    return render(request, 'dashboard/basico/estados_form.html', {'form': form, 'page_title': 'Editar Estado'})

@login_required
def estados_delete(request, pk):
    estado = get_object_or_404(Estado, pk=pk)
    if request.method == 'POST':
        try:
            estado.delete()
            messages.success(request, 'Estado removido com sucesso!')
            return redirect('dashboard:estados')
        except Exception as e:
            messages.error(request, f'Erro ao deletar estado: {e}')
    return render(request, 'dashboard/basico/estados_confirm_delete.html', {'object': estado, 'page_title': 'Excluir Estado'})

# Views para Cidades
@login_required
def cidades(request):
    from .search_forms import CidadeSearchForm
    search_form = CidadeSearchForm(request.GET)
    cidades_list = Cidade.objects.select_related('estado', 'estado__pais').all()

    if search_form.is_valid():
        if search_form.cleaned_data.get('nome'):
            cidades_list = cidades_list.filter(nome__icontains=search_form.cleaned_data['nome'])
        if search_form.cleaned_data.get('estado'):
            cidades_list = cidades_list.filter(estado=search_form.cleaned_data['estado'])

    paginator = Paginator(cidades_list, 15)  # 15 cidades por página
    page_number = request.GET.get('page')
    cidades = paginator.get_page(page_number)

    context = {
        'page_title': 'Cidades',
        'cidades': cidades,
        'search_form': search_form,
    }
    return render(request, 'dashboard/basico/cidades.html', context)

@login_required
def cidades_create(request):
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cidade criada com sucesso!')
            return redirect('dashboard:cidades')
        else:
            messages.error(request, 'Erro ao criar a cidade.')
    else:
        form = CidadeForm()
    return render(request, 'dashboard/basico/cidades_form.html', {'form': form, 'page_title': 'Nova Cidade'})

@login_required
def cidades_update(request, pk):
    cidade = get_object_or_404(Cidade, pk=pk)
    if request.method == 'POST':
        form = CidadeForm(request.POST, instance=cidade)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cidade atualizada com sucesso!')
            return redirect('dashboard:cidades')
        else:
            messages.error(request, 'Erro ao atualizar a cidade.')
    else:
        form = CidadeForm(instance=cidade)
    return render(request, 'dashboard/basico/cidades_form.html', {'form': form, 'page_title': 'Editar Cidade'})

@login_required
def cidades_delete(request, pk):
    cidade = get_object_or_404(Cidade, pk=pk)
    if request.method == 'POST':
        try:
            cidade.delete()
            messages.success(request, 'Cidade removida com sucesso!')
            return redirect('dashboard:cidades')
        except Exception as e:
            messages.error(request, f'Erro ao deletar cidade: {e}')
    return render(request, 'dashboard/basico/cidades_confirm_delete.html', {'object': cidade, 'page_title': 'Excluir Cidade'})
