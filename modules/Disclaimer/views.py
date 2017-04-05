from django.shortcuts import render
from django.http import HttpResponse
from .models import Sitio, Status

# Create your views here.

# Vista para dashboard Disclaimer
# Calcula número total de sitios, iniciados, terminados, en proceso, suspendidos
# Por región
def Index(request):
	sitioxRegion = []

	# Sitios Asignados Por Región
	sitioxRegion.append(Sitio.objects.filter(coordinador_mastec__exact='Oscar').count())
	sitioxRegion.append(Sitio.objects.filter(coordinador_mastec__exact='Luis Gutierrez').count())
	sitioxRegion.append(Sitio.objects.filter(coordinador_mastec__exact='Lino De La Rosa').count())
	sitioxRegion.append(Sitio.objects.filter(coordinador_mastec__exact='Alfonso Merlos').count())

	# ToDo Sitios iniciados
	# ToDo Sitios Terminados
	# ToDo Sitios En Proceso
	# ToDo Sitios Entregados

	return render(request,'Disclaimer/index_disclaimer.html',{'sitioxRegion': sitioxRegion})


def Sitiosxregion(request, region):

	if region == "Guerrero":
		coord_mastec='Oscar'
	elif region =="Morelos":
		coord_mastec='Luis Gutierrez'
	elif region =="Tabasco":
		coord_mastec='Lino De La Rosa'
	elif region =="Yucatan":
		coord_mastec='Alfonso Merlos'

	sitios = Sitio.objects.filter(coordinador_mastec__exact=coord_mastec)

	return render(request,'Disclaimer/sitiosxregion_disclaimer.html',{'sitios': sitios, 'region': region})
