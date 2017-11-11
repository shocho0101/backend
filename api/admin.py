from django.contrib import admin
from .models import Account
# Register your models here.
from .models import Group, Homework

admin.site.register(Account)

@admin.register(Group)
class Group(admin.ModelAdmin):
    pass

@admin.register(Homework)
class Homework(admin.ModelAdmin):
    pass

