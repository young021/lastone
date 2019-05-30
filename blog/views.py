from django.shortcuts import render,redirect
#redirect 어떤 처리후에 페이지를 보여주기만한. render랑 달라
from .models import Blog
from .forms import BlogForms
from django.contrib.auth.decorators import login_required


#view를 통해 알려주므로 모든 함수랑 form을 적어야함.

# Create your views here.
def home(request):
    blog_all = Blog.objects.all #퀘리셋, 퀘리셋 처리: 매소드 // 
    context = {'blog_all':blog_all}
    return render(request,'home.html', context) #render 함수에 넣어줌
    
def new(request):

    if request.method == "POST":  ##method 를 post로 보냄.
       forms=BlogForms(request.POST)                         #저장해주기
       if forms.is_valid:
           forms.save()
           return redirect('home')


    forms=BlogForms() #forms라는 객체를 만들어줌. templates으로 보내줌. -new.html.
    return render(request,'new.html',{'forms':forms})   # new 함수 글쓰기를 누르면 다른페이지로 이동하게 설정.

#@loginrequired  이건 어떤함수에 권한을 주는거. 