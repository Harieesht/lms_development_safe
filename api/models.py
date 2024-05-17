from django.db import models

class College(models.Model):
    name=models.CharField(max_length=300,verbose_name='NAME')
    
class Department(models.Model):
    name=models.CharField(max_length=300,verbose_name='DEPARTMENTNAME')
    years=models.YearField()
    college=models.ForeignKey(College,on_delete=models.PROTECT,verbose_name=College)
    
class Course(models.Model):
    name=models.CharField(max_length=300,verbose_name='NAME')
    description=models.TextField(verbose_name='Description')
    department=models.ForeignKey(Department,on_delete=models.PROTECT,verbose_name='Department')
    
    
class CourseItem(models.Model):
    name=models.CharField(max_length=300,verbose_name='Name')
    description=models.TextField()
    
class CourseItemList(models.Model):
    description=models.TextField()
    pdf=models.FileField(upload_to='pdffiles')
    ppt=models.FileField(upload_to='ppt')
    video=models.FileField(upload_to='video')
    
    
    
    
    
