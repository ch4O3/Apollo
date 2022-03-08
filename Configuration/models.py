from django.db import models

# Create your models here.
from django.db import models
from django.utils.html import format_html


class Configuration(models.Model):
    id = models.AutoField(primary_key=True, db_column="id", verbose_name='序号')
    name_choices = (
        ("1", "VT接口"),
        ("2", "钉钉接口"),
        ("3", "Github接口"),
        ("4", "钟馗接口"),
        ("5", "佛法接口"),
        ("6", "线程数"),
        ("7", "系统地址"),
        ("8", "系统域名"),
        ("9", "常用端口"),
        ("10", "关键端口")
    )
    name = models.CharField(unique=True, max_length=2, choices=name_choices, verbose_name='配置名称')
    user = models.CharField(db_column="user", max_length=128, verbose_name='用户名', null=True, blank=True)
    value = models.CharField(db_column="value", max_length=512, verbose_name='Token令牌', null=True, blank=True)
    port = models.TextField(db_column="port", verbose_name='端口列表', null=True, blank=True)
    ipaddress = models.GenericIPAddressField(db_column="ipaddress", verbose_name='系统地址', null=True, blank=True, default="127.0.0.1")
    domain = models.CharField(db_column="domain", max_length=256, verbose_name='系统域名', default="apollo.local", null=True, blank=True)
    count = models.IntegerField(db_column="count", verbose_name='配置值', default=10, null=True, blank=True)
    timestamp = models.DateField(db_column="timestamp", verbose_name='创建日期')

    def __str__(self):
        for item in self.name_choices:
            if self.name == item[0]:
                return item[1]

    def change(self):
        btn_str = '<a class="btn btn-xs btn-danger" href="{}">' \
                  '<input name="编辑"' \
                  'type="button" id="passButton" ' \
                  'title="passButton" value="编辑">' \
                  '</a>'
        return format_html(btn_str, '%s/change' % self.id)

    change.short_description = '配置编辑'

    class Meta:
        verbose_name = '配置信息'
        verbose_name_plural = verbose_name