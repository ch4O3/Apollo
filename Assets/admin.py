from django.db import transaction
from django.contrib import admin, messages
from Assets.models import AssetTask, AssetList


# Register your models here.
admin.site.site_header = '阿波罗自动化攻击评估系统'  # 设置header
admin.site.site_title = '阿波罗自动化攻击评估系统'  # 设置title


@admin.register(AssetTask)
class AssetTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'top_level_domain', 'port_scan_type', 'timestamp', 'change']
    list_filter = ['top_level_domain', 'timestamp']
    search_fields = ['name', 'top_level_domain']
    ordering = ["id"]
    date_hierarchy = 'timestamp'

    @transaction.atomic
    def scan(self, request, queryset):
        work_ids = None
        for item in request.POST.lists():
            if item[0] == "_selected_action":
                work_ids = item[1]
        if isinstance(work_ids, list):
            for work_id in work_ids:
                # thread = Scan(work_id)
                # thread.start()
                messages.add_message(request, messages.SUCCESS, '开始扫描%s' % str(work_id))
        else:
            messages.add_message(request, messages.SUCCESS, '扫描异常')

    scan.short_description = "启动扫描"
    scan.icon = 'fa fa-rocket'
    scan.style = 'color:white;'
    scan.type = 'danger'
    scan.confirm = '您确定要启动扫描吗？'
    actions = [scan, ]


@admin.register(AssetList)
class AssetListAdmin(admin.ModelAdmin):
    list_display = ['id', 'ip_address', 'top_level_domain', 'system', 'port', 'state', 'protocol', 'service',
                    'software', 'version', 'middle_ware', 'timestamp', 'change']
    list_filter = ['ip_address', 'top_level_domain', 'system', 'port', 'state', 'protocol', 'service', 'software',
                   'middle_ware', 'timestamp']
    search_fields = ['ip_address', 'top_level_domain', 'subdomain', 'cname', 'system', 'port', 'state', 'protocol',
                     'service', 'software', 'middle_ware']
    ordering = ["id"]
    date_hierarchy = 'timestamp'

