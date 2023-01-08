from django.db import models
from django.utils.translation import gettext as _
# Create your models here.


class Foods(models.Model):
    FOOD_TYPE=[
        ('drinks','نوشیدنی'),
        ('dinner','صبحانه'),
        ('lunch','غذای اصلی'),
    ]
    
    name  = models.CharField(_('اسم'), max_length=50)
    info  = models.CharField(_('توضیحات'),max_length=100)
    rate  = models.IntegerField (_("امتیاز"),default=0)
    price = models.IntegerField(_('قیمت'))
    time  = models.IntegerField(_("زمان آماده شدن"))
    date  = models.DateField(_("تاریخ ثبت"),auto_now=False,auto_now_add=True)
    photo = models.ImageField(upload_to='food_images/')
    type_food = models.CharField(_('نوع خوراکی'),max_length=10,choices=FOOD_TYPE,default='drink')
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = ' غذا'
        verbose_name_plural = 'غذاها'