
#! from django.contrib import admin
# from .models import Student,Aadhar
# # Register your models here.
# admin.site.register(Student)
#! admin.site.register(Aadhar)


#! from django.contrib import admin
# from .models import StudentModel, DepartmentModel
# # Register your models here.

# class Department(admin.ModelAdmin):
#     list_display = ['id','dep_name','description']
# admin.site.register(DepartmentModel,Department)

# class Student(admin.ModelAdmin):
#     list_display = ['id','stu_name','stu_class','stu_email','stu_mobile','stu_department']
#! admin.site.register(StudentModel,Student)

from django.contrib import admin
from .models import FuelTypeModel,CarModel
# Register your models here.

# admin.site.register(FuelTypeModel)
# admin.site.register(CarModel)

class Fuel(admin.ModelAdmin):
    list_display = ('id', 'fuel_name')
admin.site.register(FuelTypeModel,Fuel)

class Car(admin.ModelAdmin):
    list_display = ('id','car_name')
admin.site.register(CarModel,Car)