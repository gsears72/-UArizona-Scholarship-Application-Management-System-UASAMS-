from django.contrib import admin
from Login.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class UserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'username', 'First_name', 'Last_name','Net_ID','role','is_admin','is_staff','last_login']
    search_fields = ['email', 'username', 'First_name', 'Last_name','Net_ID','role','is_admin','is_staff','last_login']
    readonly_fields = ['last_login']

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password','username','First_name','Last_name','Net_ID','Security_Question1','Security_Question1_answer','Security_Question2',
                       'Security_Question2_answer','role','is_admin','is_staff','is_superuser')}),
    )
    
    

admin.site.register(User, UserAdmin)
