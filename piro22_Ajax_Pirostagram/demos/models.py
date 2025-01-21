from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    like = models.IntegerField()
    photo = models.ImageField('이미지', upload_to='posts/%Y%m%d', blank=False)
   

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0) 