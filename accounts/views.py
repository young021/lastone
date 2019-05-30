#이것은 두번째 app accoutns
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
#ㅇdjango 에서 제공하는 form 

# Create your views here.
def signup(request):
    if request.method=="POST": 
       signup_form=UserCreationForm(request.POST)
       if signup_form.is_valid:
          signup_form.save()
          return redirect('home')
       else:
           return redirect('signup')

    signup_form=UserCreationForm() #class 생성하는 객체값 signupform 
    return render(request,'registration/signup.html',{'signup_form':signup_form})
