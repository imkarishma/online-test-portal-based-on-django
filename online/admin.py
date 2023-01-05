from django.contrib import admin
from .models import Question,Detail
# Register your models here.

@admin.register(Question)
class AdminQuestion(admin.ModelAdmin):
    list_display=['queno','question','optiona','optionb','optionc','optiond','answer','category','user']

@admin.register(Detail)
class AdminDetail(admin.ModelAdmin):
    list_display=['user','name','institute','degree','branch','image','points','solved','correct','worng']