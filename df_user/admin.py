# coding=UTF-8
from django.contrib import admin
# Register your models here.
from .models import UserInfo


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'uname', 'uphone']  # 显示这三个字段
    list_filter = ['uphone']  # 过滤字段
    search_fields = ['uname']  # 搜索字段


admin.site.register(UserInfo,UserInfoAdmin)