from fastapi import APIRouter
from fastapi_amis_admin.admin import AdminApp


def setup(router: APIRouter, admin_app: AdminApp, **kwargs):
    # 导入相关模块
    from . import admin, apis, jobs

    # 注册路由
    router.include_router(apis.router, prefix='/suetactix', tags=['suetactix'])
    # 注册管理页面
    admin_app.register_admin(admin.SuetactixApp)

