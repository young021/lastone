from django.db import models
from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    
    title=models.TextField(max_length=200)
    body=models.TextField() 
    pub_date=models.DateField(default=timezone.now)
    #published_date=models.DateField(default=timezone.now)
    
 

    def __str__(self): #객체의 반환값을 객체의 타이틀로 
                    #이거 없음 안됨.
        return self.title #파이썬 내부제공함수.
