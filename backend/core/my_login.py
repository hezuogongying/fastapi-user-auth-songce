from fastapi_user_auth.admin.admin import UserLoginFormAdmin, UserRegFormAdmin
from fastapi.responses import HTMLResponse
from fastapi_amis_admin.utils.translation import i18n as _
from starlette.requests import Request
from jinja2 import Environment, FileSystemLoader


# 创建 Jinja2 环境
template_env = Environment(loader=FileSystemLoader('templates'))


# 创建一个自定义的登录表单管理员
class CustomUserLoginFormAdmin(UserLoginFormAdmin):

    async def get_page(self, request: Request) -> HTMLResponse:
        page = await super().get_page(request)

        # 获取表单
        form = await self.get_form(request)

        # 准备 HTML 模板数据
        template_data = {
            'form': form
        }

        # 渲染 HTML 模板
        template = template_env.get_template('login.html')
        html_content = template.render(template_data)

        return HTMLResponse(content=html_content, status_code=200)

# 创建一个自定义的注册表单管理员
class CustomUserRegFormAdmin(UserRegFormAdmin):

    async def get_page(self, request: Request) -> HTMLResponse:
        page = await super().get_page(request)

        # 获取表单
        form = await self.get_form(request)

        # 准备 HTML 模板数据
        template_data = {
            'form': form
        }

        # 渲染 HTML 模板
        template = template_env.get_template('register.html')
        html_content = template.render(template_data)

        return HTMLResponse(content=html_content, status_code=200)

# 其他配置...