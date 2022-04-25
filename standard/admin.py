from django.contrib import admin

from .models import AppliedStds, Specialty1, Specialty2, Specialty3, SpecialtyStd, UploadModel

# Register your models here.
admin.site.register(UploadModel)
admin.site.register(AppliedStds)
admin.site.register(SpecialtyStd)
admin.site.register(Specialty1)
admin.site.register(Specialty2)
admin.site.register(Specialty3)