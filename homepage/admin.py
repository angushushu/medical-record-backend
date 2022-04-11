from django.contrib import admin

# Register your models here.
from .models import Charge, Homepage, LesionReason, MainDiag, OtherDiag, Op, Pathology, PostAdmitComa, PreAdmitComa
# Register your models here.
admin.site.register(Homepage)
admin.site.register(MainDiag)
admin.site.register(LesionReason)
admin.site.register(Pathology)
admin.site.register(PreAdmitComa)
admin.site.register(PostAdmitComa)
admin.site.register(OtherDiag)
admin.site.register(Op)
admin.site.register(Charge)