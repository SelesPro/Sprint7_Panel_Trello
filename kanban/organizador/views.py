from django.shortcuts import render,redirect,get_object_or_404
from django.forms import ModelForm
from organizador.models import Tarea,Tablero,Lista


# Create your views here.


class TableroForm(ModelForm):
	class Meta:
		model = Tablero
		fields = ['creartablero']

def index(request):
    return render(request, "organizador/index.html", {})

def consultartablero(request):
	plantilla = 'organizador/consultartablero.html'
	form = TableroForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = TableroForm()
	listadotablero = Tablero.objects.all()
	contexto={'object_list' : listadotablero, 'form':form}
	return render (request, plantilla, contexto)

def infotablero(request,id):
	plantilla= 'organizador/infotablero.html'
	form = ListaForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ListaForm()
	tableros = Tablero.objects.prefetch_related('listas__tareas')
	infotablero= get_object_or_404(tableros,pk=id)
	#infotablero= infotablero.prefetch_related('listas__tareas')
	contexto={'info':infotablero, 'form':form}
	return render(request,plantilla,contexto)

class ListaForm(ModelForm):
	class Meta:
		model = Lista
		fields = ['nombreLista','fkTablero']


class TareaForm(ModelForm):
    class Meta:
        model = Tarea
        fields = ['nombre', 'descripcion','fkLista']
def creartarea(request):
	plantilla='organizador/creartarea.html'
	form = TareaForm(request.POST or None)
	if form.is_valid():
		form.save()
		#return redirect('aplilibreria:consultarcliente')aqui colocamos donde queramos redirigir
	return render(request,plantilla,{'form':form})





