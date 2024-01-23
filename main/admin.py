from django.contrib import admin
from.models import *

class PostAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, PostAdmin)
admin.site.register(Category, PostAdmin)