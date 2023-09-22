from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from.models import Yellow,Green
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.
@admin.register(Yellow)
class AdminView(ImportExportActionModelAdmin):

    class Meta:
        model=Yellow

@admin.register(Green)
class Admin(ImportExportActionModelAdmin):

    class Meta:
        model=Green