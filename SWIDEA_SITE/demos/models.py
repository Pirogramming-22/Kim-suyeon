from django.db import models

class devTool(models.Model):
    name=models.TextField()
    kind=models.TextField()
    content=models.TextField()

    def __str__(self):
        return self.name


