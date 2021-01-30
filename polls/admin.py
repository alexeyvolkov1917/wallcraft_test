from django.contrib import admin
from .models import Employee, Position, Department


# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.get_fields()] + ['iswork']
    list_filter = ('department', 'position')
    fieldsets = (('Информация о работнике', {'fields': (('first_name', 'last_name'), 'second_name', 'birth_date')}),
                 ('Контактная информация', {'fields': (('email', 'phone_number'),)}),
                 ('Работа', {'fields': (('start_work_date', 'end_work_date'), ('position', 'department'))}))


class PositionAdmin(admin.ModelAdmin):
    list_display = ('position',)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department',)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Department, DepartmentAdmin)
