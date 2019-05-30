"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import blog.views
from accounts import views as ac_views #이것은 애칭.
from django.contrib.auth.views import LoginView, LogoutView  #장고내의 로그인로그아웃 들고오기.
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static 



urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',blog.views.home,name='home'),
    path('new/',blog.views.new, name="new"), # 블로그의 view안에 new 라는 함수를 실행.
    path('',ac_views.signup,name="signup"),
    path('accounts/login/', LoginView.as_view(),name="login"),
    path('logout/', LogoutView.as_view(),name="logout"),

    path('portfolio',portfolio.views.portfolio, name="portfolio"), #이렇게 ()앞에 비어있으면 제일 시작페이지가 됨.
    

] #CBV: Class Based View, FBV: Function  BAsed View

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
