from django.shortcuts import render,redirect
from my_app.models import BlogModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth import authenticate, login, logout


def detail_view(request,slug):

    obj1 = BlogModel.objects.get(slug=slug)

    context = {
    'obj1':obj1
    }
    return render(request,'blog-detail.html',context)


def blog_view(request):

    blogs = BlogModel.objects.filter(reading_count__gte=5)

    context = {
         'blogs':blogs,
            
           }
    return render(request,'blog.html',context)

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog')
        
    context = {}

    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("blog")

