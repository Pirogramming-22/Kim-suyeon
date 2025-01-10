from django.shortcuts import render,redirect
from .models import Create
from django.urls import reverse

def create(request):
    if request.method=='POST':
        create=Create.objects.create(
            title=request.POST['title'],
            year=request.POST['year'],
            genre=request.POST['genre'],
            rating=request.POST['rating'],
            time=request.POST['time'],      
            review = request.POST['review'],               
            director = request.POST['director'],
            actor = request.POST['actor'],
        )
        return redirect(reverse('movie:index'))
    return render(request, 'create.html')