from datetime import date
from typing import Optional

from fastapi_amis_admin.models.fields import Field
from fastapi_user_auth.admin import AuthAdminSite, RoleAdmin, UserAuthApp
from fastapi_user_auth.auth.models import BaseRole, BaseUser

# 需要安装sqlmodelx. pip install sqlmodelx
class MyUser(BaseUser, table=True):
    point: int = Field(default=0, title="积分", description="用户积分")
    phone: str = Field("", title="手机号", max_length=15)
    parent_id: Optional[int] = Field(None, title="上级", foreign_key="auth_user.id")
    birthday: Optional[date] = Field(None, title="出生日期")
    location: str = Field("", title="位置")
    __table_args__ = {'extend_existing': True}

class MyRole(BaseRole, table=True):
    __tablename__ = "auth_role"  # 数据库表名,必须是这个才能覆盖默认模型
    icon: str = Field("", title="图标")
    is_active: bool = Field(default=True, title="是否激活")
    __table_args__ = {'extend_existing': True}
    

class MyRoleAdmin(RoleAdmin):
    model = MyRole


# class MyUserRoleLink(UserRoleLink, CreateTimeMixin, table=True):
#     # 重写UserRoleLink模型, 并且创建id虚拟主键字段
#     id: str = Field(
#         None, title="虚拟主键",
#         sa_column=column_property(
#             # 注意这里的cast, 用于将联合主键转换为字符串.不要使用format, 会导致直接识别为字符串.
#             cast(UserRoleLink.user_id, String) + "-" + cast(UserRoleLink.role_id, String)
#         )
#     )
#
#     description: str = Field(None, title="描述")


class MyUserAuthApp(UserAuthApp):
    RoleAdmin = MyRoleAdmin


class MyAuthAdminSite(AuthAdminSite):
    UserAuthApp = MyUserAuthApp
