from django.contrib import admin
from my_app.models import BlogModel,BlogImage,Hashtag

# Register your models here.

class imageinline(admin.StackedInline):
    model = BlogImage
    extra = 1

class BlogAdmin(admin.ModelAdmin):
    list_display = ('slug','name')
    inlines = [imageinline]

admin.site.register(BlogModel,BlogAdmin)   
admin.site.register(Hashtag)