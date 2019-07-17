from django.shortcuts import render,redirect
from .models import Blogdata
from django.contrib.auth.models import User
# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')


def blogpost(request, id):
    if request.method == 'POST':
        a = User.objects.get(id=id)
        title = request.POST['title']
        body = request.POST['body']
        email = a.email
        obj = Blogdata(title=title, body=body, email=email)
        obj.save()
        return redirect('home')
    else:
        return render(request, 'blog/blog_post.html')

def blogview(request):
    obj = Blogdata.objects.all()
    return render(request, 'blog/blog_view.html', {'result':obj})


def blogviewall(request):
    obj = Blogdata.objects.all()
    return render(request, 'blog/blog_view_all.html', {'result':obj})

def blogedit(request, id):
    a = Blogdata.objects.get(id=id)

    return render(request, 'blog/blog_edit.html', {'result': a})


def blogupdate(request, id):
    a = Blogdata.objects.get(id=id)
    a.title = request.POST['title']
    a.body = request.POST['body']
    a.save()
    return redirect('blogview')