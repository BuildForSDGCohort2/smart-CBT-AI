from django.contrib import admin
from .models import Result_Obj, Result_Theory, Result

# Register your models here.
admin.site.register(Result_Obj)
admin.site.register(Result_Theory)
admin.site.register(Result)