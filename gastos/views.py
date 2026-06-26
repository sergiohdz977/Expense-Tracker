from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Gasto
from .forms import GastoForm
from django.db.models import Sum
from django.contrib import messages
from .forms import FiltroFechaForm

# Create your views here.

def home(request):
    form = FiltroFechaForm(request.GET)
    gastos = Gasto.objects.all()
    if form.is_valid():
        desde = form.cleaned_data.get('desde')
        hasta = form.cleaned_data.get('hasta')
        if desde and hasta:
            gastos = gastos.filter(fecha__range=[desde, hasta])
    total = Gasto.objects.aggregate(Sum('monto'))
    return render(request, 'gastos/home.html', {"gastos": gastos, "total" : total['monto__sum'], "form": form})

def agregar_gasto(request):
    if request.method == "POST":
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Gasto guardado correctamente')
            return redirect('home')
    else:
        form = GastoForm()
    return render(request, 'gastos/agregar.html', {"form" : form})

def eliminar_gasto(request, id):
    gasto = Gasto.objects.get(id = id)
    gasto.delete()
    return redirect('home')

def editar(request, id):
    gasto = Gasto.objects.get(id=id)
    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid:
            form.save()
            messages.success(request, 'Gasto editado correctamente')
            return redirect('home')
    else:
        form = GastoForm(instance=gasto)
    context = {'form': form}
    return render(request, 'gastos/editar.html', context)

    





    


