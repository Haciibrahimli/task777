from django.db import models
from services.mixin import SlugMixin, DateMixin
from services.uploader import Uploader
from services.generator import Generator


class BlogModel(SlugMixin,DateMixin):
    name = models.CharField(max_length=255,verbose_name='blog adi')
    main_image = models.ImageField(upload_to=Uploader.upload_photo_to_blog,null=True,blank=True)
    subject = models.TextField(verbose_name='movzu')
    reading_count = models.CharField(max_length=255,verbose_name='oxuma sayi')

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
    
