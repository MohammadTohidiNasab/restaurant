from django.db import models
from django.utils.translation import gettext as _
from django.utils import timezone  
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    description = models.CharField(_("توضیحات"), max_length=100)
    content = models.TextField(_("متن"))
    created_at = models.DateTimeField(_(""), default=timezone.now)
    auther = models.ForeignKey(User, verbose_name=_("نویسنده"), on_delete=models.CASCADE)
    image  = models.ImageField(_("تصویر"), upload_to="blogsImg/")
    category = models.ForeignKey("Category",related_name='blog', verbose_name=_("دسته بندی"),on_delete=models.PROTECT)
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    title = models.CharField(_("عنوان"), max_length=50)
    slug  = models.SlugField(_("عنوان انگلیسی"))
    published_at = models.DateTimeField(_("تاریخ انتشار") ,auto_now=False , auto_now_add=True)

    def __str__(self):
        return self.title