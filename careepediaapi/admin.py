from django.contrib import admin
from .models import Intermediate, Bachelor
from import_export.admin import ImportExportModelAdmin

# Register your models here.
# admin.site.register(Intermediate)
# admin.site.register(Bachelor)


@admin.register(Bachelor, Intermediate)
class ViewAdmin(ImportExportModelAdmin):
    pass
