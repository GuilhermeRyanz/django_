from django.contrib import admin

from client import models

# Register your models here.
class  ClientAdmin(admin.ModelAdmin):
     list_display = ('id', 'name', 'age')
     search_fields = ('name', 'age')
     list_filter = ('name', 'age')
     list_display_links = ('id', 'name', 'age')
     list_per_page = 20

     def has_add_permission(self, request):
         return True

     def has_delete_permission(self, request, obj=None):
         return True

     def has_change_permission(self, request, obj=None):
         return True

admin.site.register(models.Client, ClientAdmin)