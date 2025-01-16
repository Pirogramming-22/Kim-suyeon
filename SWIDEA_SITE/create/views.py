from django.shortcuts import render,redirect
from .models import Post
from django.urls import reverse
from demos.models import devTool
from django.http import HttpResponse

def register(request):
    if request.method=='POST':
        selected_tool_id = request.POST.get('tool')
        selected_tool = devTool.objects.get(id=selected_tool_id)
        create=Post.objects.create(
            title=request.POST['title'],
            img=request.FILES['img'],
            content=request.POST['content'],
            interest=request.POST['interest'],
            tool=selected_tool,
        )
        return redirect(reverse('demos:main'))
    tools = devTool.objects.all()
    return render(request, 'create/register.html', {'tools': tools})



def toggle_star(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)  
        post.is_starred = not post.is_starred 
        post.save()
    except Post.DoesNotExist:
        return redirect('demos:main') 
    return redirect('demos:main')  

def update_interest(request, post_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        post = Post.objects.get(pk=post_id)

        if action == 'increase':
            post.interest += 1
        elif action == 'decrease':
            post.interest -= 1

        post.save()
        return HttpResponse(post.interest)
    return HttpResponse(status=400)