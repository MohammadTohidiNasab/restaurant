from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone  
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=100)
    content = models.TextField(_("متن"))
    created_at = models.DateTimeField(_("تاریخ ایجاد"), default=timezone.now)
    auther = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image  = models.ImageField(_("تصویر"), upload_to="blogsImg/")
    category = models.ForeignKey("Category",related_name='blog', verbose_name=_("دسته بندی"),on_delete=models.PROTECT)
    tags = models.ManyToManyField("Tag",related_name='blog', verbose_name=_("تگ ها"))
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'وبلاگ'
        verbose_name_plural = 'وبلاگ ها'
    
class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug  = models.SlugField(_("عنوان انگلیسی"))
    published_at = models.DateTimeField(_("تاریخ انتشار") ,auto_now=False , auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'
    
    
    
class Tag(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug = models.SlugField(_("عنوان لاتین"))
    published_at = models.DateTimeField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)
    updated_at = models.DateField(_("تاریخ  بروز رسانی"), auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = ' تگ'
        verbose_name_plural = ' تگ ها '
    
    
class Comment(models.Model):
    blog = models.ForeignKey("blog", verbose_name=_("مقاله"),related_name='comments' ,on_delete=models.CASCADE)
    name = models.CharField(_("نام کاربر"), max_length=100) 
    email = models.EmailField(_("ادرس الکترونیکی"), max_length=254)        
    massage = models.TextField(_("متن نظر"))
    date = models.DateField(_("تاریخ ثبت"), auto_now=False, auto_now_add=True)
    def __str__(self):
       return self.email
        
            
    class Meta:
        verbose_name = ' نظر '
        verbose_name_plural = ' نظرات '