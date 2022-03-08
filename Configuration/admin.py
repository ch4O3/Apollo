from django.contrib import admin

from Configuration.models import Configuration
# Register your models here.
admin.site.site_header = '阿波罗自动化攻击评估系统'  # 设置header
admin.site.site_title = '阿波罗自动化攻击评估系统'          # 设置title
@admin.register(Configuration)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'value', 'count', 'port', 'ipaddress', 'domain', 'timestamp', 'change']
    list_filter = ['name', 'timestamp']
    search_fields = ['name', 'user']
    ordering = ["id"]
    date_hierarchy = 'timestamp'
