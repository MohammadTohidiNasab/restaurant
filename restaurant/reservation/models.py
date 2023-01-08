from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Reservation(models.Model):
    name  = models.CharField(_('نام و نام خانوادگی'),max_length=200)
    email = models.EmailField(_("ایمیل "), max_length=254)
    phone = models.CharField(_("شماره تلفن"),max_length=15)
    date  = models.DateField(_("تاریخ"), auto_now=False, auto_now_add=False)
    time  = models.TimeField(_("زمان"), auto_now=False, auto_now_add=False)
    number= models.IntegerField(_('تعداد'))
    
    def __str__(self):
        return self.name
    
        
    class Meta:
        verbose_name = ' رزرو '
        verbose_name_plural = ' رزرو شده ها '