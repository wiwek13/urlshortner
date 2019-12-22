
from django.db import models
from django.conf import settings
# Create your models here.
from .utils import code_generator, create_shortcode

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)

class WirrURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_m = super(WirrURLManager,self).all(*args,**kwargs)
        qs = qs_m.filter(active=True)
        return qs
    def refresh_shortcodes(self,item=None):

        qs = WirrURL.objects.filter(id__gte=1)
        new_code = 0
        if item is not None and isinstance(item,int):
            qs = qs.order_by('-id')[:item]

        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_code +=1
        return "Newcodes mades {i}".format(i=new_code)


class WirrURL(models.Model):
    url = models.CharField(max_length=220, )
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateField(auto_now=True)
    timestamp = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = WirrURLManager()
    test = WirrURLManager()
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode=="":
            self.shortcode = create_shortcode(self)
        super(WirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
