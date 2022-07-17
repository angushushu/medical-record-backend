from django.contrib import admin

from settlement.models import MainOp, OtherOp, Settlement, PostAdmitComa, PreAdmitComa

# Register your models here.
admin.site.register(Settlement)
admin.site.register(MainOp)
admin.site.register(OtherOp)
admin.site.register(PreAdmitComa)
admin.site.register(PostAdmitComa)