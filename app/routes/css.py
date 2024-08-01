from fastapi import APIRouter, Request
from starlette.templating import Jinja2Templates


# 라우터 생성
css_router = APIRouter()
# 템플릿 지정
templates = Jinja2Templates(directory='views/templates')


@css_router.get('/')
async def semantic(req: Request):
    return templates.TemplateResponse('css/index.html', {'request': req})


@css_router.get('/selector')
async def selector(req: Request):
    return templates.TemplateResponse('css/01selector.html', {'request': req})

@css_router.get('/reset')
async def reset(req: Request):
    return templates.TemplateResponse('css/02reset.html', {'request': req})

@css_router.get('/text')
async def text(req: Request):
    return templates.TemplateResponse('css/03text.html', {'request': req})

@css_router.get('/box')
async def box(req: Request):
    return templates.TemplateResponse('css/04box.html', {'request': req})

@css_router.get('/list')
async def list(req: Request):
    return templates.TemplateResponse('css/05list.html', {'request': req})

@css_router.get('/position')
async def list(req: Request):
    return templates.TemplateResponse('css/06position.html', {'request': req})

@css_router.get('/background')
async def list(req: Request):
    return templates.TemplateResponse('css/07background.html', {'request': req})
