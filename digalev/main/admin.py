from django.contrib import admin
from .models import Category, Service, Equipment, CompletedWorks, User, Order


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Equipment, CompletedWorks)
class Admin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category', )
    prepopulated_fields = {
        'slug': ('name', )
    }


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_published')
    list_filter = ('category', 'is_published')
    prepopulated_fields = {
        'slug': ('name', )
    }


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'telephone', 'is_mudak')



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('description', 'date_created', 'user', 'plan_file')
    date_hierarchy = 'date_created'
    search_fields = ('description',)

