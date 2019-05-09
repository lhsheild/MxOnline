from .models import EmailVerifyRecord, Banner

from extra_apps import xadmin
from xadmin import views


class BaseSetting():
    enable_themes = True
    use_bootswatch = True


class GlobalSetting():
    site_title = 'sheildog_MxOnline'
    site_footer = 'sheildog_MxOnline'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['id', 'email', 'code', 'send_time']
    search_fields = ['id', 'email', 'code', 'send_type']
    list_filter = ['id', 'email', 'code', 'send_type', 'send_time']


class BannerAdmin():
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
