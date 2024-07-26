from fastapi import APIRouter, Request, Form
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates
from app.schema.emp import Employee
from datetime import date

# HTML 관련 라우트를 위한 APIRouter 인스턴스 생성
emp_router = APIRouter()

# 템플릿 설정
templates = Jinja2Templates(directory='views/templates')

# HTML 관련 뷰의 홈 라우트
@emp_router.get('/emp', response_class=HTMLResponse)
async def emp(req: Request):
    return templates.TemplateResponse('emp/emp.html', {'request': req})

# Employee 데이터를 수신하는 라우트
@emp_router.post('/emp_result', response_class=HTMLResponse)
async def empok(req: Request,
                          empid: str = Form(...),fname: str = Form(...), lname: str = Form(...),
                          email: str = Form(...), phone: str = Form(...),
                          hdate: date = Form(...), jobid: str = Form(...),
                          sal: int = Form(...), comm: float = Form(...),
                          mgrid: int = Form(...), deptid: int = Form(...)):
    # 입력받은 데이터를 사용하여 Employee 객체 생성
    emp = Employee(
        empid=empid,
        fname=fname, lname=lname, email=email, phone=phone,
        hdate=hdate, jobid=jobid, sal=sal, comm=comm,
        mgrid=mgrid, deptid=deptid
    )
    # 템플릿 렌더링과 함께 데이터를 전달
    return templates.TemplateResponse('emp/emp_result.html', {'emp': emp, 'request': req})