import datetime
from django.shortcuts import render,HttpResponse
from django.views.generic import View
from .forms import Myform, Mytlp, Mypwd, Modify
from font.models import User, Book, Telephone
from django.db.models import Q


# Create your views here.

temp ={
    'telephone':'',
    'name':'',
    'pwd':'',
    'bid':'',
}

def shouye_views(request,cid=-1):
    if cid < 0:
        book = Book.objects.all()
        return render(request, 'book.html', {'book':book})
    else:
        book = Book.objects.filter(id=cid)
        return render(request,'details.html',{'book':book})

def shouye_views1(request,bid=-1):

    if bid < 0:
        return render(request,'book.html')
    else:
        temp['bid']=bid
        return render(request,'modify.html')


class modify_views(View):
    '''修改处理'''
    def get(self,request):

        return render(request,'modify.html')

    def post(self,request):
        form = Modify(request.POST,request.FILES)
        logo =request.FILES.get('logo')
        name = request.POST.get('bname')
        author = request.POST.get('author')
        feilei = request.POST.get('fenlei')
        details = request.POST.get('details')
        # return HttpResponse(logo)
        if form.is_valid():
            book = Book.objects.filter(id=temp['bid'])
            if 'logo' in request.FILES:
                book = Book(id=temp['bid'])
                book.bname=name
                book.author=author
                book.fenlei=feilei
                book.content=details
                book.addtime= datetime.datetime.now()
                book.logo=logo
                book.save()
                return HttpResponse('修改成功')
            else:
                return HttpResponse('123')

        else:
            return HttpResponse('fail')
class register_views(View):
    '''注册 '''
    def get(self,request):

            return render(request,'zhuce.html')

    def post(self,request):
        '''验证注册手机号'''
        formd = Mytlp(request.POST)
        telephone = request.POST.get('telephone')
        yzm = request.POST.get('yzm')
        yzms = '8TS2'

        if formd.is_valid():
            if telephone and yzm:
                num = Telephone.objects.filter(telephone=telephone).count()
                if num ==1 and yzm == yzms:
                    return HttpResponse('手机号码已存在！')
                elif num ==1 and yzm !=yzms:
                    return HttpResponse('验证码错误！')
                else:
                    temp['telephone']=telephone
                    t = Telephone()
                    t.telephone=telephone
                    t.save()
                    return  render(request,'zhuce.html')
        else:
            return HttpResponse('请输入有效的手机号码！')

def return_views(request):
    deletes =Telephone.objects.get(telephone=temp['telephone'])
    deletes.delete()
    return render(request,'zhuce.html')

class register1_views(View):
    '''注册处理'''
    def get(self,request):

        return render(request,'zhuce1.html')

    def post(self,request):
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        pwd1 = request.POST.get('password1')
        if name:
            num = User.objects.filter(username=name).count()
            if num ==1:
                return HttpResponse('用户名已存在！')
            else:
                if pwd == pwd1:
                    u = User()
                    u.username=name
                    u.password=pwd1
                    u.telephone=Telephone.objects.get(telephone=temp['telephone'])
                    u.save()
                    return render(request,'zhuceSucc.html')
                else:
                    return HttpResponse('前后输入的密码不一致！')

class IndexView(View):
    '''登录处理'''
    def get(self,request):

        return render(request,'index.html')


    def post(self,request):
        form = Myform(request.POST)
        names = request.POST.get('username')
        pwd = request.POST.get('password')
        yzm =request.POST.get('yanzhen')
        yzms = '8TS2'
        if form.is_valid():
            if names and pwd:
                num = User.objects.filter(username=names,password=pwd).count()
                if num ==1 and yzm ==yzms:
                    temp['name']=names
                    return render(request, 'book.html')
                elif num==1 and yzm != yzms:
                    return HttpResponse('验证码不正确！')
                else:
                    return  HttpResponse("用户不存在或密码不正确！")
        else:
            print(form.errors.get_json_data())
            return HttpResponse('fail')

class pwd_views(View):
    '''忘记密码处理类'''
    def get(self,request):

        return render(request,'password.html')

    def post(self,request):
        form = Mytlp(request.POST)
        telephone = request.POST.get('telephone')
        if form.is_valid():
            num = Telephone.objects.filter(telephone=telephone).count()
            if num == 1:

                temp['telephone']=telephone
                return render(request,'password_2.html')
        else:
            return HttpResponse('fail')

class pwd_views2(View):
    '''忘记密码处理类'''
    def get(self,request):

        return render(request,'password_2.html')

    def post(self,request):
        form = Mypwd(request.POST)
        pwd = request.POST.get('pwd')
        pwd2 = request.POST.get('pwd2')
        yzm = request.POST.get('yzm')

        if form.is_valid():
            if pwd:
                num = Telephone.objects.get(telephone=temp['telephone'])
                id = num.id
                user = User.objects.get(telephone_id=id)
                user.password = pwd2
                user.save()
                return render(request,'zhuceSucc.html')
        else:
            return HttpResponse('fail')



