from django.contrib import admin
from .models import project, tasks

# Register your models here.
admin.site.register(project)
admin.site.register(tasks)
