from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from user import views
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.
def index(request):

    messages.error(request, "porra,  que merda cara")
    return render(request, 'index.html')

@login_required(login_url='login')
def dashboard(request, pk):
    return render(request, 'dashboard.html')


@login_required(login_url='login')
def topics(request):
    # filter(owner=request.user) -> retorna apenas o topicos que foram criado pelo ussuraio logado
    """mostra todos os assuntos"""

    topics = Topic.objects.filter(owner=request.user).order_by('date')
    
    #filtra uma quantidade de assuntos por pagina
    topic_paginator = Paginator(topics, 5) #--> objeto que deve aparecer na pagina, e a qunatidade
    page_num = request.GET.get('page') #--> o Django está se situando em qual página da paginação ele está.
    page = topic_paginator.get_page(page_num) #--> verifica o que deve mostrar na pagina

    context = {'page': page}
    return render(request, 'learning-logs/topics.html', context)


@login_required(login_url='login')
def topic(request, pk):
    """mostra um unico assunto e todas as suas entradas"""
    topic = Topic.objects.get(id=pk)
    """garante que o assunto pertence ao ususario atual"""
    if topic.owner != request.user:
        raise Http404 #404 é uma resposta padrão, devolvidsa quando o dado requisitado não existe no servidor

    entries = topic.entry_set.order_by('-date_added')
    entry_paginator = Paginator(entries, 5)
    page_num = request.GET.get('page')
    page = entry_paginator.get_page(page_num)

    contexto = {'topic': topic, 'page':page}
    return render(request, 'learning-logs/topic.html', contexto)

@login_required(login_url='login')
def new_topic(request):
    """adiciona um novo assunto"""

    if request.method != 'POST':
        # nenhum dado submetido, exibe um formulario em branco
        form = TopicForm

    else:
        # dados foram submentidos, recupera por meio do post, processa os dados 
        form = TopicForm(request.POST)
        
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user #dentro do novo topico, vai buscar o propiretario para associar
            new_topic.save()
            return redirect('topics')

    context = {'form': form}

    return render (request, 'learning-logs/new_topic.html', context)

@login_required(login_url='login')
def new_entry(request, pk):

    topic = Topic.objects.get(id=pk)
    
    if request.method == 'get':
        form = EntryForm()

    else:
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topic', pk=topic.pk)
    context = {'topic': topic, 'form': form}
    return render(request, 'learning-logs/new_entry.html', context)

@login_required(login_url='login')
def edit_entry(request, pk):
    """edita uma entrada existente"""
    entry = Entry.objects.get(pk=pk)
    topic = entry.topic
    #entry.topic: Acessa o atributo topic do objeto entry. 
    #Presumivelmente, o modelo Entry possui um campo chamado topic, e essa linha de código está recuperando o valor desse campo para armazená-lo na variável topic.
    if topic.owner != request.user:
        raise Http404
    # request.POST or none --> se existir dados para processar, processa, se nao, apenas passa pra frente e exibe os dados do form (instance=entry)
    form = EntryForm(request.POST or None, instance=entry) 
    if form.is_valid():
        form.save()   
        return redirect('topic', pk=topic.pk)
    context = {
        'entry': entry,
        'topic': topic,
        'form': form
        }
    return render(request, 'learning-logs/edit_entry.html', context)


@login_required(login_url='login')
def delete_topic(request, pk):

    dado = get_object_or_404(Topic, pk=pk)


    dado.delete()

    return redirect('topics')

@login_required(login_url='login')
def delete_entry(request, pk):

    dado = get_object_or_404(Entry, pk=pk)


    dado.delete()

    return redirect('topics')

def paginator(request):

    topics = Topic.objects.all()

    topic_paginator = Paginator(topics, 3)
    page_num = request.GET.get('page')
    page = topic_paginator.get_page(page_num)

    return render(request, 'learning-logs/topics.html', {'page': page})
@login_required(login_url='login')
def videocall(request):

    context = {
        'name': request.user
    }
    return render(request, 'video-conference/videocall.html', context)
def new_meeting(request):

    pass


def join_meeting(request):

    pass