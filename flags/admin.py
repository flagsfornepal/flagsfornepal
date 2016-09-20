from django.contrib import admin

from .models import Flag

def approve(FlagAdmin, request, queryset):
	queryset.update(state="approved")
approve.short_description = "Approve selected flags"

class FlagAdmin(admin.ModelAdmin):
	list_display = ('admin_thumb', 'state', 'flagReason', 'tagline', 'name', 'location')
	actions = [approve]

	
admin.site.register(Flag, FlagAdmin)