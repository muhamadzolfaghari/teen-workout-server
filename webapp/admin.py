from django.contrib import admin
from .models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ('user_id', 'age_ranges', 'gender')


admin.site.register(User , UserAdmin)