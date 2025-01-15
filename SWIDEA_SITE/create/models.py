from django.db import models
from demos.models import devTool



class Post(models.Model):
    title=models.TextField()
    img = models.ImageField('이미지', upload_to='posts/%Y%m%d', blank=True)
    content=models.TextField()
    interest=models.IntegerField('아이디어 관심도', default=0)
    tool = models.ForeignKey(devTool, on_delete=models.CASCADE, related_name='posts') 
    is_starred = models.BooleanField(default=False) 
    
    def __str__(self):
        return self.title

