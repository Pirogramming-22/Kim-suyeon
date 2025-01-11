from django.shortcuts import render,redirect
from create.models import Create
from django.urls import reverse

def index(request):
    creates=Create.objects.all()
    context={
        'creates': creates
    }
    return render(request, 'index.html',context)

def review(request):
    return render(request, 'index.html')

def detail(request, pk):
    movie=Create.objects.get(id=pk)
    context={
        'movie': movie
    }
    return render(request, 'detail.html', context)

def update(request, pk):
    movie=Create.objects.get(id=pk)
    if request.method=="POST":
        title2=request.POST.get('title')
        year2=request.POST.get('year')
        time2=request.POST.get('time')
        rating2=request.POST.get('rating')
        review2=request.POST.get('review')
        director2=request.POST.get('director')
        actor2=request.POST.get('actor')
        genre2=request.POST.get('genre')
        movie.title=title2
        movie.year=year2
        movie.time=time2
        movie.rating=rating2
        movie.review=review2
        movie.director=director2
        movie.actor=actor2
        movie.genre=genre2
        movie.save()
        return redirect('movie:detail', pk=movie.pk)
    context={
        'movie':movie
    }
    return render(request, 'update.html', context)

def delete(request, pk):
    if request.method=='POST':
        movie=Create.objects.get(id=pk)
        movie.delete()
        return redirect('movie:index')