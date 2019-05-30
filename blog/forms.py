from django import forms
#model 을 가져와야하니까
from .models import Blog

class BlogForms(forms.ModelForm):
  
    class Meta:
        model=Blog
        fields =('title','body','pub_date')
        #블로그 form 은 어떤것인지 명찰처럼 붙여주는 것.
        #내부클래스 선언.