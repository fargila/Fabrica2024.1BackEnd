import requests
from AppDesafio.models import Atividade 
from django.shortcuts import render, redirect
from django import forms

def alocarDadosAPI(request):
    
    response = requests.get('https://www.boredapi.com/api/activity')
    data = response.json()
    if isinstance(data, dict):
        Instancia = Atividade(
            activity=data.get('activity', 1),
            type=data.get('type', 2),
            participants=data.get('participants', 3),
            price=data.get('price', 4),
            link=data.get('link', 5),
            key=data.get('key', 6),
            acessibility=data.get('acessibility', 7)
        )
        Instancia.save()
    elif isinstance(data, list):
        for i in data:
            Instancia = Atividade(
                activity=i.get('activity'),
                type=i.get('type'),
                participants=i.get('participants'),
                price=i.get('price'),
                link=i.get('link'),
                key=i.get('key'),
                acessibility=i.get('acessibility')
            )
            Instancia.save()

    return render(request, 'FabricaDesafio\templates\home.html', {'data': data})

def addDado(request):
    class CreateAtiv(forms.ModelForm):
        class Meta:
            modelo = Atividade
            campos = ['activity', 'type', 'participants', 'price', 'link', 'key', 'acessibility']
        
    if request.method == 'POST':
        form = CreateAtiv(request.POST)
        if form.is_valid():
            activity = form.cleaned_data['activity']
            if CreateAtiv.objects.filter(activity=activity).exists():
                form.add_error('Essa atividade já está presente no banco de dados')
            else:
                form.save()    
            return redirect('Sucesso')
        else:
            return redirect('Erro, aconteceu alguma coisa')
    else:
        form = CreateAtiv()
    return render(request, "FabricaDesafio\templates\add.html", {'form': form})

def buscarAtiv(request):
    if(request.method == 'GET'):
        query = request.GET.get('query')
        results = Atividade.objects.filter(name__icontains=query)
        return render(request, "FabricaDesafio\templates\busca.html", {'results':results})


