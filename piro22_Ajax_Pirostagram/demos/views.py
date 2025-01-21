from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm

def main(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'demos/pirostagram.html', ctx)



def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save() 
            return redirect('demos:main')  
        else:
            print(form.errors)
            return render(request, 'demos/post_create.html', {'form': form})
    else:
        form = PostForm()
        return render(request, 'demos/post_create.html', {'form': form})
    
def post(request, pk):
    datail=Post.objects.get(id=pk)
    context={
        'detail': datail
    }
    return render(request, 'demos/post.html', context)

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req.get('id')
    button_type = req.get('type')

    post = Post.objects.get(id=post_id)

    if button_type == 'like':
        post.like += 1
    else:
        post.like += 1
    post.save()

    return JsonResponse({'id': post_id, 'type': button_type, 'like': post.like})



@csrf_exempt
def comment_ajax(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        post_id = req.get('id')
        comment_text = req.get('comment')

        post = get_object_or_404(Post, id=post_id)

        comment = Comment.objects.create(post=post, content=comment_text)

        comment_count = Comment.objects.filter(post=post).count()

        return JsonResponse({
            'id': post_id,
            'comment': {
                'id': comment.id,
                'content': comment.content,
            },
            'comment_count': comment_count,  
        })


@csrf_exempt
def delete_comment_ajax(request):
    if request.method == 'POST':
        req = json.loads(request.body)
        post_id = req.get('id')
        comment_id = req.get('comment_id')

        post = get_object_or_404(Post, id=post_id)
        comment = Comment.objects.filter(id=comment_id, post=post).first()

        if comment:
            comment.delete()
        else:
            return JsonResponse({'error': 'Comment not found'}, status=404)

        comment_count = Comment.objects.filter(post=post).count()

        return JsonResponse({'id': post_id, 'comment_count': comment_count})
