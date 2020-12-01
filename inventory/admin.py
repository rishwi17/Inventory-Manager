from django.contrib import admin
from .models import Furniture,Fashion,Gadgets
# Register your models here.
@admin.register(Furniture,Fashion,Gadgets)
class PersonAdmin(admin.ModelAdmin):
    pass