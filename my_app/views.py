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

    blog = request.GET.get('blog') #search
    if blog is not None:
       blogs = blogs.filter(title__icontains = blog)

    paginator = Paginator(blogs, 1) #pagination
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)

    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
 

    context = {
         'blogs':blogs,
         'p':p     
           }
    return render(request,'blog.html',context)
