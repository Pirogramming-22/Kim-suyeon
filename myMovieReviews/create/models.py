from django.db import models

class Create(models.Model):
    title = models.TextField() 
    year = models.TextField()     
    genre = models.TextField()   
    rating = models.DecimalField(max_digits=5, decimal_places=1)  
    time = models.TextField()      
    review = models.TextField()               
    director = models.TextField()  
    actor = models.TextField()     

    
