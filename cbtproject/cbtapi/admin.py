from django.contrib import admin
from .models import Objective
from .models import Theory

# Register your models here.
admin.site.register(Objective)
admin.site.register(Theory)