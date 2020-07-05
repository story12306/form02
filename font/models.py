from django.db import models
from font.forms import Myform
# Create your models here.
class User(models.Model):
    '''用户类'''
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    telephone = models.ForeignKey(to='Telephone',on_delete=models.CASCADE)

    class Meta:
        db_table= 'user'

    def __str__(self):

        return "<用户:({username},{password},{telephone})>".format(username=self.username,password=self.password,telephone=self.telephone)

class Telephone(models.Model):
    telephone = models.CharField(max_length=255)



class Book(models.Model):
    '''图书模型'''
    bname = models.CharField(max_length=255,verbose_name='书籍')
    author = models.CharField(max_length=255,verbose_name='作者')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    fenlei = models.CharField(max_length=255,verbose_name='分类')
    content = models.TextField(verbose_name='内容')
    logo = models.ImageField()

    class Meta:
        db_table = 'book'
        verbose_name_plural='书籍'


class Index(models.Model):
    classification =models.CharField(max_length=100)

    class Meta:
        db_table = 'classification'