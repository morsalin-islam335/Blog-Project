from django.contrib import admin

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}# dictionary key is slug_field and value is slug field apply field
    display = ['slug', 'name']

from . import models
admin.site.register(models.Category, CategoryAdmin)



