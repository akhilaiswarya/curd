from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.PositiveIntegerField(primary_key=True)
    dname=models.CharField(max_length=20)
    loc=models.CharField(max_length=20)

    def __str__(self):
        return str(self.deptno)
    
class Emp(models.Model):
    empno=models.PositiveIntegerField()
    ename=models.CharField(max_length=20)
    job=models.CharField(max_length=20)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename

class Salgrade(models.Model):
    ename=models.CharField(max_length=20)
    sal=models.PositiveIntegerField()

    def __str__(self):
        return self.ename

class Bonus(models.Model):
    ename=models.CharField(max_length=20)
    bonus=models.PositiveIntegerField()

    def __str__(self):
        return str(self.bonus)


    


    
    

    