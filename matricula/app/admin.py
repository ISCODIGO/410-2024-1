from django.contrib import admin

# Register your models here.
from app.models import Periodo


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    pass
