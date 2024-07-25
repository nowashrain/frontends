from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates

# HTML 관련 라우트를 위한 APIRouter 인스턴스 생성
html_router = APIRouter()

# 템플릿 설정
templates = Jinja2Templates(directory='views/templates')

# HTML 관련 뷰의 홈 라우트
@html_router.get('/')
async def home(req: Request):
    # HTML 인덱스 페이지 렌더링
    return templates.TemplateResponse('html/index.html', {'request': req})

# 레이아웃 예제 라우트
@html_router.get('/layout')
async def show_layout(req: Request):
    # 레이아웃 예제 페이지 렌더링
    return templates.TemplateResponse('html/01layout.html', {'request': req})
