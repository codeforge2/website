from django.contrib import admin
from .models import dev_group

# Register your models here.
class My_dev_admin(admin.ModelAdmin):
    list_display = ('name','Tech_stack', 'email', 'Mobile_num')

admin.site.register(dev_group,My_dev_admin)

