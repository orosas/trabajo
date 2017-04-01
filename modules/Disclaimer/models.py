from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# blank= True significa si el campo requiere ingresar algún dato en los forms para su validación
# es decir, si es True no será requerido
class Sitio(models.Model):
	region = models.CharField(max_length=3, null=True)
	gerente_att = models.CharField(max_length=50, null=True, blank=True)
	coordinador_att = models.CharField(max_length=50, null=True, blank=True)
	cellowner = models.CharField(max_length=50, null=True, blank=True)
	telefono_cellowner = models.CharField(max_length=50, null=True, blank=True)
	coordinador_mastec = models.CharField(max_length=50, null=True)
	ciudad = models.CharField(max_length=50, null=True, blank=True)
	idatt_mastec = models.CharField(max_length=50, null=True)
	site_id = models.CharField(max_length=20, null=True, blank=True)
	id3g = models.CharField(max_length=20, null=True)
	idgsm = models.CharField(max_length=20, null=True)
	idlte = models.CharField(max_length=20, null=True)
	ididen = models.CharField(max_length=20, null=True)
	lat_decimal = models.DecimalField(max_digits=9, decimal_places=6, null=True)
	long_decimal = models.DecimalField(max_digits=9, decimal_places=6, null=True)
	nombre_sitio = models.CharField(max_length=50)
	prioridad = models.CharField(max_length=2, null=True)
	jerarquia = models.CharField(max_length=30, null=True)
	sitios_dependientes = models.CharField(max_length=20, null=True)
	comentarios_att = models.TextField(null=True, blank=True)
	cluster = models.CharField(max_length=50, null=True)
	problema_acceso = models.TextField(null=True, blank=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_sitio')
	actualizado = models.DateField(auto_now=True)
	creado = models.DateField(auto_now_add=True)

	class Meta:
		permissions = (("contra_view", "Contratista Can View"),
						("mastec_view", "Mastec Can View"),
					   )

	def __str__(self):
		return u"%s %s" % ("Sitio: ", self.nombre_sitio)

ACTIVIDAD = (
	('NOSS', 'Por Levantar'),
	('SS', 'Levantado'),
	('CWS', 'Proceso CW'),
	('CWF', 'Terminado CW'),
	('CWF', 'Entregado'),
	)

STATUS = (
	('OK', 'Activo'),
	('CA', 'Cancelado'),
	('SU', 'Suspendido'),
	)

class Status(models.Model):
	sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='status')
	ultima_actividad = models.CharField(choices=ACTIVIDAD, max_length=10)
	avance = models.PositiveSmallIntegerField(null=True)
	status = models.CharField(choices=STATUS, max_length=30)
	creado = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_status')

	class Meta:
		permissions = (("contra_view", "Contratista Can View"),
						("mastec_view", "Mastec Can View"),
					   )

	def __str__(self):
		return u"%s" % (self.sitio)

class Levantamiento(models.Model):
	sitio = models.ForeignKey(Sitio,on_delete=models.CASCADE, related_name='levantamientos')
	ss_sem_att = models.PositiveSmallIntegerField(null=True, blank=True)
	ss_programado = models.DateField(null=True, blank=True)
	ss_real = models.DateField(null=True, blank=True)
	ss_hechox = models.CharField(max_length=50, null=True, blank=True)
	ss_nota = models.TextField(null=True, blank=True)
	ss_recibido = models.DateField(null=True, blank=True)
	ss_validacion = models.DateField(null=True, blank=True)
	creado = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_ss')

	class Meta:
		permissions = (("contra_view", "Contratista Can View"),
						("mastec_view", "Mastec Can View"),
					   )

	def __str__(self):
		return u"%s" % (self.sitio)

SUPERVISOR = (
		('OL', 'Oscar López'),
		('PQ', 'Pablo Quezada'),
		('FJ', 'Francisco Juárez'),
		('MS', 'Miguel Salgado'),
		('LG', 'Luis Gutierrez'),
		('OM', 'Oscar Marín'),
		('LD', 'Lino De La Rosa'),
		('JP', 'Juan Pablo Flores'),
		('ME', 'Martín Elías'),
		('JG', 'Jaime García'),
		('GJ', 'Gerardo Jiménez'),
		('AB', 'Arturo Bautista'),
		('AS', 'Antonio Salazar'),

	)

# Lista de proveedores para campo choices de class Mantenimiento y 
# class Profile
PROVEEDOR = (
		('DH', 'David Hernández'),
		('EKSA', 'ECCASA'),
		('ETL', 'ECOTEL'),
		('FS', 'Franco & Soto'),
		('FD', 'Freddy'),
		('GICOM', 'Grupo ICOM'),
		('GIP', 'Grupo IPE'),
		('GVI', 'Grupo VALBRI'),
		('GST', 'Grupo SET'),
		('JAVCRUZ', 'Javier De La Cruz'),
		('JAVJ', 'Javier Jiménez'),
		('JJ', 'Juan Jesús'),
		('MC', 'Macario Hernández'),
		('MQ', 'Maqueda'),
		('VK', 'Ve-Ca'),
		('VI', 'Viadeza'),
	)

class Mantenimiento(models.Model):
	sitio = models.ForeignKey(Sitio,on_delete=models.CASCADE, related_name='mnto')
	proveedor = models.CharField(choices=PROVEEDOR, max_length=50, null=True, blank=True)
	supervisor = models.CharField(choices=SUPERVISOR, max_length=50, null=True, blank=True)
	cuadrilla = models.CharField(max_length=50, null=True, blank=True)
	cos_sem_att = models.PositiveSmallIntegerField(null=True, blank=True)
	cos_programado =  models.DateField(null=True, blank=True)
	cos_real = models.DateField(null=True, blank=True)
	cof_sem_att = models.PositiveSmallIntegerField(null=True, blank=True)
	cof_programado = models.DateField(null=True, blank=True)
	cof_real = models.DateField(null=True, blank=True)
	creado = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name='users_mnt')

	class Meta:
		permissions = (("contra_view", "Contratista Can View"),
						("mastec_view", "Mastec Can View"),
					   )

	def __str__(self):
		return u"%s" % (self.sitio)

class Volumetrico(models.Model):
	sitio = models.ForeignKey(Sitio,on_delete=models.CASCADE, related_name='sitio_presupto')
	volPre_recepcion = models.DateField(null=True, blank=True)
	vol_po_solitada = models.DateField(null=True, blank=True)
	vol_po_monto = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
	vol_final_recibido = models.DateField(null=True, blank=True)
	vol_final_vobo = models.CharField(choices=SUPERVISOR, max_length=50, null=True, blank=True)
	vol_envio_att = models.DateField(null=True, blank=True)
	vol_monto_venta = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
	vol_valida_att = models.DateField(null=True, blank=True)
	vol_creado = models.DateField(auto_now_add=True)
	usuario = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_presupto')

	class Meta:
		permissions = (("contra_view", "Contratista Can View"),
						("mastec_view", "Mastec Can View"),
					   )

	def __str__(self):
		return u"%s" % (self.sitio)

class Profile(models.Model):
	usuario = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile')
	es_contrata = models.BooleanField(default=True)
	contrata_view = models.BooleanField(default=False)
	mastec_admin = models.BooleanField(default=False)
	proveedor = models.CharField(choices=PROVEEDOR, max_length=50, null=True, blank=True)


	class Meta:
		permissions = (("contra_view", "Contratista Can View"),
						("mastec_view", "Mastec Can View"),
					   )

# ToDo 
"""
¿¿¿¿¿¿¿Control de PO's de contratistas??????
¿¿¿¿¿¿¿Agregar a modelo volumétricos?????




para checar permisos de usuarios en View

if request.user.has_perm('app_name.can_add_cost_price')

ó se puede usar:

@login_required
@permission_required('polls.can_vote', raise_exception=True)
def my_view(request):
..............


Si es que en Models:

class Meta:
        permissions = (
            ("can_add_cost_price", "Can add cost price"),
        )


31-MAR-2017: Completar lista de proveedores


"""