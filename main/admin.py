from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import User, Company, Person, Survey, Surveyor, Outlet, Publication, Question, Answer



class CustomUserAdmin(UserAdmin):    
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    exclude = ('first_name', 'last_name', 'username',)
    readonly_fields = ('date_joined',)
    list_display = ['email','is_staff','is_active','date_joined']
    list_filter = ('is_staff',)
    fieldsets = (
        ('Personal info', {'fields': ('email', 'password')}),
        ('Important dates', {'fields': ('date_joined',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    list_display = ('email', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(User,CustomUserAdmin)
admin.site.register(Company)
admin.site.register(Person)
admin.site.register(Surveyor)
admin.site.register(Outlet)
admin.site.register(Survey)
admin.site.register(Publication)
admin.site.register(Question)
admin.site.register(Answer)





# Register your models here.
