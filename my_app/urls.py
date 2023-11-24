from django.urls import path
from my_app.views import detail_view,blog_view

urlpatterns = [


path('blog/',blog_view,name = 'blog'),
path('detail/<slug>/',detail_view,name = 'detail'),
]