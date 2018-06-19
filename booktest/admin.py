from django.contrib import admin

# Register your models here.

from .models import BookInfo  # python3 需要 .models 这样引入  python2 直接 models
from .models import HerInfo


class HerInfoInline(admin.StackedInline):
    # class HerInfoInline(admin.TabularInline):#表格形式
    model = HerInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):  # 管理表显示修改
    list_display = ['pk', 'btitle', 'bpub_date']  # 显示这三个字段
    list_filter = ['btitle']  # 过滤字段
    search_fields = ['btitle']  # 搜索字段
    fields = ['bpub_date', 'btitle']  # 属性的先后顺序
    inlines = [HerInfoInline]  # 关联


class HerInfoAdmin(admin.ModelAdmin):
    list_display = ['pk', 'hname', 'gender']
    list_per_page = 10  # 分页
    fieldsets = [('basic', {'fields': [ 'hname', 'hgender']}),  # 将字段分组
                 ('more', {'fields': ['hcontent', 'hBook']})]


admin.site.register(HerInfo, HerInfoAdmin)
admin.site.register(BookInfo, BookInfoAdmin)
