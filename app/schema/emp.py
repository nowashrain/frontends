from pydantic import BaseModel
from datetime import date


class Employee(BaseModel):
    empid : str
    fname : str
    lname : str
    email : str
    phone : str
    hdate : date
    jobid : str
    sal   : int
    comm  : float
    mgrid : int
    deptid : int