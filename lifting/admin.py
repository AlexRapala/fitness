from django.contrib import admin
from lifting import models

# Register your models here.
admin.site.register(models.Log)
admin.site.register(models.Lift)
admin.site.register(models.LogXLift)