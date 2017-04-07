from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Sitio, Status
from django.db.models import Q
from .forms import BusquedaForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

# Vista para dashboard Disclaimer
# Calcula número total de sitios, iniciados, terminados, en proceso, suspendidos
# Por región
def Index(request, error=False):
	sitioxRegion = []
	print("Si estoy adentro de Index Disclaimer:")
	# Sitios Asignados Por Región
	sitioxRegion.append(Sitio.objects.filter(coordinador_mastec__exact='Oscar').count())
	sitioxRegion.append(Sitio.objects.filter(coordinador_mastec__exact='Luis Gutierrez').count())
	sitioxRegion.append(Sitio.objects.filter(coordinador_mastec__exact='Lino De La Rosa').count())
	sitioxRegion.append(Sitio.objects.filter(coordinador_mastec__exact='Alfonso Merlos').count())

	# ToDo Sitios iniciados
	# ToDo Sitios Terminados
	# ToDo Sitios En Proceso
	# ToDo Sitios Entregados

	form = BusquedaForm()
	elerror = error

	return render(request,'Disclaimer/index_disclaimer.html',{'sitioxRegion': sitioxRegion, 'form': form, 'elerror': elerror})


# view que lista todos los sitios de una región (Guerrero, Morelos, Tabasco, Yucatán)
# utiliza template Disclaimer/sitiosxregion_disclaimer.html
def lista_Sitiosxregion(request, region):

	if region == "Guerrero":
		coord_mastec='Oscar'
	elif region =="Morelos":
		coord_mastec='Luis Gutierrez'
	elif region =="Tabasco":
		coord_mastec='Lino De La Rosa'
	elif region =="Yucatan":
		coord_mastec='Alfonso Merlos'

	# En Queryset sólo están los campos
	sitios_lista = Sitio.objects.only('idatt_mastec','nombre_sitio','region','coordinador_mastec','cellowner').filter(coordinador_mastec__exact=coord_mastec)

	paginator = Paginator(sitios_lista, 5)

	page = request.GET.get('page')

	try:
		sitios = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		sitios = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		sitios = paginator.page(paginator.num_pages)

	form = BusquedaForm()

	return render(request,'Disclaimer/sitiosxregion_disclaimer.html',{'sitios': sitios, 'region': region, 'form': form})

# Búsqueda de Sitios
# recibe párametro de formulario en barra de navegación de template base.html
def Busqueda_Sitio(request):

	if request.method == 'POST':
		form = BusquedaForm(request.POST)
		if form.is_valid():
			q = form.cleaned_data['q']

			sitios = Sitio.objects.filter(Q(nombre_sitio__icontains=q)|
											Q(idatt_mastec__icontains=q)
				)

			#print("String recibido: " + q)

			#sitios = Sitio.objects.filter(nombre_sitio__icontains=q)

			for sitio in sitios:
				print("sitio PK: " + str(sitio.pk))
			
			return render(request, 'Disclaimer/sitiosxregion_disclaimer.html', {'sitios':sitios, 'form': form})

			#return HttpResponse("El string recibido es: " + q)


		else:
			elerror = True
			return redirect('Disclaimer:index-disclaimer', elerror)
	else:
		form = BusquedaForm()
		return render(request, 'Disclaimer/index_disclaimer.html', {'form': form})
