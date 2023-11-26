from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.uploader import Uploader
from services.generator import Generator

class Hashtag(DateMixin):
    name = models.CharField(max_length= 255,verbose_name='tag adi')

    def __str__(self):
       return self.name
    
    class Meta:
       ordering = ('created_at',)
       verbose_name = 'hastag'
       verbose_name_plural = 'hastaglar'


class BlogModel(SlugMixin,DateMixin):
    name = models.CharField(max_length=255,verbose_name='blog adi')
    main_image = models.ImageField(upload_to=Uploader.upload_photo_to_blog,null=True,blank=True)
    subject = models.TextField(verbose_name='movzu')
    reading_count = models.IntegerField(verbose_name='oxuma sayi',null=True,blank=True)
    hastags = models.ManyToManyField(Hashtag)
    def __str__(self):
        return self.name
    class Meta:

     ordering = ('name',)
     verbose_name = 'movzu'
     verbose_name_plural = 'movzular'

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=BlogModel)
        super(BlogModel, self).save(*args, **kwargs)
    
class BlogImage(DateMixin,SlugMixin):
    blog = models.ForeignKey(BlogModel,on_delete=models.SET_NULL,null=True,blank=True)
    image = models.ImageField(upload_to=Uploader.upload_photo_to_blog)
    
     
    def __str__(self):
        return self.blog.name
    class Meta:

     ordering = ('-created_at',)
     verbose_name = 'blog sekili'
     verbose_name_plural = 'blog sekilleri'

    def save(self, *args, **kwargs):
        if not self.slug:
         self.slug = Generator.create_slug_shortcode(size=10, model_=BlogImage)
        super(BlogImage, self).save(*args, **kwargs)

