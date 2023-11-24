from django.shortcuts import render
from my_app.models import BlogModel
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def detail_view(request,slug):

    obj1 = BlogModel.objects.get(slug=slug)

    context = {
    'obj1':obj1
    }
    return render(request,'blog-detail.html',context)


def blog_view(request):

    blogs = BlogModel.objects.all()

    context = {
         'blogs':blogs,
            
           }
    return render(request,'blog.html',context)
