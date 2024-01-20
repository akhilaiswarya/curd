from django.shortcuts import render
from app.models import *
from django.http import HttpResponse


# Create your views here.
def display_dept(request):
    QLDO=Dept.objects.all()
    d={'dept':QLDO}
    return render(request,'display_dept.html',d)

def insert_dept(request):
    dt=int(input('enter deptno:'))
    dn=input('enter dept name:')
    lc=input('enter location:')
    DTO=Dept.objects.get_or_create(deptno=dt,dname=dn,loc=lc)[0]
    DTO.save()
    return HttpResponse('deptno is inserted')




def display_emp(request):
    QLEO=Emp.objects.all()
    QLEO=Emp.objects.filter(empno__gt=100)
    QLEO=Emp.objects.filter(empno__lt=100)
    QLEO=Emp.objects.filter(empno__gte=77)
    QLEO=Emp.objects.filter(empno__lte=101)
    QLEO=Emp.objects.filter(ename__startswith='S')
    QLEO=Emp.objects.filter(ename__endswith='g')
    QLEO=Emp.objects.filter(ename__contains='t')
    d={'emp':QLEO}
    return render(request,'display_emp.html',d)

def insert_emp(request):
    eno=int(input('enter empno:'))
    en=input('enter ename')
    j=input('enter job:')
    dt=int(input('enter deptno'))
    do=Dept.objects.get(deptno=dt)
    ETO=Emp.objects.get_or_create(empno=eno,ename=en,job=j,deptno=do)[0]
    ETO.save()
    return HttpResponse('empno is inserted')


