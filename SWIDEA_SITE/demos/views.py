from django.shortcuts import render, redirect
from create.models import Post
from demos.models import devTool
from django.urls import reverse

def main(request):
    sort = request.GET.get('sort', 'default')
    if sort == 'star':
        create = Post.objects.filter(is_starred=True).order_by('-interest')  
    elif sort == 'name':
        create = Post.objects.all().order_by('title')  
    elif sort == 'created':
        create = Post.objects.all().order_by('id')  
    elif sort == 'latest':
        create = Post.objects.all().order_by('-id')  
    else:
        create = Post.objects.all()  

    context = {
        'create': create,
        'sort': sort,
    }
    return render(request, 'demos/index.html', context)

def ideaDetail(request, pk):
    datail=Post.objects.get(id=pk)
    context={
        'detail': datail
    }
    return render(request, 'demos/ideaDetail.html', context)

def ideaDelete(request, pk):
    if request.method=='POST':
        create=Post.objects.get(id=pk)
        create.delete()
        return redirect('demos:main')

def ideaUpdate(request, pk):
    create = Post.objects.get(id=pk)  
    if request.method == "POST":
        title2 = request.POST.get('title', create.title)
        img2 = request.FILES.get('img')  
        content2 = request.POST.get('content', create.content)
        interest2 = request.POST.get('interest', create.interest)
        tool_id = request.POST.get('tool')

        try:
            selected_tool = devTool.objects.get(id=tool_id)  # 선택된 tool의 인스턴스 가져오기
        except devTool.DoesNotExist:
            selected_tool = create.tool 

        create.title = title2
        create.content = content2
        create.interest = interest2
        create.tool = selected_tool
        create.img=img2
        create.save()
        return redirect('demos:ideaDetail', pk=create.pk)
    tools = devTool.objects.all() 
    context = {
        'create': create,
        'tools': tools
    }
    return render(request, 'demos/ideaUpdate.html', context)


def devToolRegister(request):
    if request.method=='POST':
        dev=devTool.objects.create(
            name=request.POST['name'],
            kind=request.POST['kind'],
            content=request.POST['content'],
        )
        return redirect(reverse('demos:devToolList'))
    return render(request, 'demos/devToolRegister.html')

def devToolList(request):
    dev=devTool.objects.all()
    context={
        'dev': dev
    }
    return render(request, 'demos/devToolList.html', context)

def devToolDetail(request, pk):
    datail=devTool.objects.get(id=pk)
    context={
        'detail': datail
    }
    return render(request, 'demos/devToolDetail.html', context)


def devDelete(request, pk):
    if request.method=='POST':
        create=devTool.objects.get(id=pk)
        create.delete()
        return redirect('demos:devToolList')


def devToolUpdate(request, pk):
    create = devTool.objects.get(id=pk)  
    if request.method == "POST":
        name2 = request.POST.get('name')
        kind2 = request.POST.get('kind')
        content2 = request.POST.get('content')
        create.name = name2
        create.content = content2
        create.kind = kind2
        create.save()
        return redirect('demos:devToolDetail', pk=create.pk)
    context = {
        'create': create
    }
    return render(request, 'demos/devToolUpdate.html', context)