from django.contrib import admin
from butler.models import *
from butler.utils import create_pages_clean_admin

@admin.register(ButlerPage)
class ButlerPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    actions = [create_pages_clean_admin]

@admin.register(FAQmodel)
class ButlerPageAdmin(admin.ModelAdmin):
    list_display = ('question',)
#admin.site.register(ButlerPage)
