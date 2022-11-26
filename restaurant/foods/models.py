from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Foods(models.Model):
    name  = models.CharField(_('اسم'), max_length=50)
    info  = models.CharField(_('توضیحات'),max_length=100)
    rate  = models.IntegerField (_("امتیاز"))
    price = models.IntegerField(_('قیمت'))
    time  = models.IntegerField(_("زمان آماده شدن"))
    date  = models.DateField(_("تاریخ ثبت"),auto_now=False,auto_now_add=True)
    photo = models.ImageField(upload_to='food_images/')
    
    def __str__(self):
        return self.name
    
