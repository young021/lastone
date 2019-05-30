from django.contrib import admin
from .models import Blog #같은 폴더내의 model 을 가지고 오고 import

# Register your models here.
admin.site.register(Blog)
