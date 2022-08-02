from django.contrib import admin

from .models import  AppliedDgStd, AppliedG2Stds, AppliedGStds, AppliedSpStd, Diag, DiagStd, G2Std, GStd, General, General1, General2, Specialty1, Specialty2, Specialty3, SpecialtyStd, UploadModel

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
# gstd
admin.site.register(AppliedG2Stds)
admin.site.register(G2Std)
admin.site.register(General1)
admin.site.register(General2)