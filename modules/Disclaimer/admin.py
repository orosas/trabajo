from django.contrib import admin
from .models import Sitio, Status, Levantamiento, Mantenimiento, Volumetrico, Profile


class SitioAdmin(admin.ModelAdmin):
	# despliega todos éstos campos en el Admin, cuando se quiere ver detalles de Post
	list_display = ('idatt_mastec', 'nombre_sitio', 'region', 'coordinador_mastec', 'cellowner' )

	# For search bar en la parte superior del admin
	search_fields = ('idatt_mastec', 'nombre_sitio',)

	# agrega una barra del lado derecho para poder filtrar los resultados
	list_filter = ('region', 'coordinador_mastec', 'ciudad' )



class StatusAdmin(admin.ModelAdmin):
	# despliega todos éstos campos en el Admin, cuando se quiere ver detalles de Post
	list_display = ('sitio', 'ultima_actividad', 'avance', 'status', 'creado',)

	# agrega una barra del lado derecho para poder filtrar los resultados
	list_filter = ('ultima_actividad', 'status', )

class MantoAdmin(admin.ModelAdmin):
	# despliega todos éstos campos en el Admin, cuando se quiere ver detalles de Post
	list_display = ('sitio', 'supervisor', 'proveedor', 'creado',)


class VolumetricoAdmin(admin.ModelAdmin):
	# despliega todos éstos campos en el Admin, cuando se quiere ver detalles de Post
	list_display = ('sitio', 'vol_po_monto', 'vol_valida_att', 'vol_creado',)

	# Despliega un lookup widget, en lugar de un dropdown menu
	raw_id_fields = ('sitio',)

# Register your models here.
admin.site.register(Sitio, SitioAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Levantamiento)
admin.site.register(Mantenimiento, MantoAdmin)
admin.site.register(Volumetrico, VolumetricoAdmin)
admin.site.register(Profile)