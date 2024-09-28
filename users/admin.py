from django.contrib import admin
#import MemberShip, CustomUser
from .models import CustomUser
from django.core.mail import send_mail
#get email from setting
from django.conf import settings
# Register your models here.

    
#search on customuser by name or email or phone 
class CustomUserAdmin(admin.ModelAdmin):
    #search fields
    search_fields = ['email','phone']
    #list display
    list_display = ['email','phone','is_staff','is_blocked']

    
    
    

admin.site.register(CustomUser,CustomUserAdmin)
