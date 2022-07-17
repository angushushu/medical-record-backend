from django.contrib import admin

from .models import  AppliedDgStd, AppliedGStds, AppliedSpStd, Diag, DiagStd, GStd, General, Specialty1, Specialty2, Specialty3, SpecialtyStd, UploadModel

# spstd
admin.site.register(AppliedSpStd)
admin.site.register(UploadModel)
admin.site.register(SpecialtyStd)
admin.site.register(Specialty1)
admin.site.register(Specialty2)
admin.site.register(Specialty3)
# dgstd
admin.site.register(AppliedDgStd)
admin.site.register(DiagStd)
admin.site.register(Diag)
# gstd
admin.site.register(AppliedGStds)
admin.site.register(GStd)
admin.site.register(General)