from django.contrib import admin
from .models import Empleado, Habilidades
# Register your models here.
admin.site.register(Habilidades)

#Cosmetic
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'id',
    )
    # Created a functio for full name
    def full_name(self,obj):
        #all operation
        print(obj.first_name)
        return obj.first_name+' '+obj.last_name

    search_fields = ('first_name',)
    list_filter = ('departamento','job', 'habilidades')
    #
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin )