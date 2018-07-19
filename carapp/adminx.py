from django.contrib import admin

# Register your models here.
import xadmin as admin
from carapp.models import UserProfile
from xadmin import views


# Register your models here.
class BaseSetting:
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    # 整体配置
    site_title = '亮亮二手车管理系统'
    site_footer = '二手车管理项目'
    menu_style = 'accordion'  # 菜单折叠
    # 搜索模型
    global_search_models = [UserProfile]

    # 模型的图标(参考bootstrap图标插件)
    global_models_icon = {
        UserProfile: "glyphicon glyphicon-user",
    }  # 设置models的全局图标


class UserProfileAdmin:
    # 后台列表显示列
    list_display = ['name', 'phone', 'email']
    # 后台列表查询条件
    search_fields = ['name', 'phone']


admin.site.register(views.CommAdminView, GlobalSettings)
admin.site.register(views.BaseAdminView, BaseSetting)

admin.site.register(UserProfile, UserProfileAdmin)
