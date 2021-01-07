from django.contrib import admin
from asApp.models import Request,Update

# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    list_display = ['Request_Type','Request_Desc','Request_Date','City','State','Pin_Code','Alternate_Phone_N',]

class UpdateAdmin(admin.ModelAdmin):
   list_display = ['Status','Remark',]

#class UpdateConfiguration(admin.TabularInline):
 #   model = Update

#class RequestConfiguration(admin.ModelAdmin):
 #   inlines = [UpdateConfiguration,]




admin.site.register(Request)
admin.site.register(Update)