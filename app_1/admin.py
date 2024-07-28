from django.contrib import admin

# Register your models here.
from .models import Proyecto, Habilidad, Educacion, Experiencia

admin.site.register(Proyecto)
admin.site.register(Habilidad)
admin.site.register(Educacion)
admin.site.register(Experiencia)
