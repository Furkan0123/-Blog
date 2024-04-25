from django.contrib import admin
from .models import Trainer , Category , Tag

admin.site.register(Trainer)



admin.site.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug' : ('name',)}


admin.site.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug' : ('name',)}