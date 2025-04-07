from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Patients)
admin.site.register(Categories_Examents)
admin.site.register(Examents)
admin.site.register(Analyses)
admin.site.register(Factures)
admin.site.register(Resultats)


