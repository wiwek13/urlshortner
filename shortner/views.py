from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import WirrURL


# Create your views here.
def testview(request):
    return HttpResponse("somestuff")


def wirrcfview(request,shortcode=None,*args,**kwargs):
    # try:
    #     obj = WirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = WirrURL.objects.all().first()

    # obj_url =None
    # qs = WirrURL.objects.get(shortcode__iexact=shortcode.upper())
    # if qs.exist() and qs.count() == 1:
    #     obj = qs.first
    #     obj_url = obj.url
    #
    obj = get_object_or_404(WirrURL,shortcode=shortcode)
    print(obj.url)
    return HttpResponseRedirect(obj.url)
    # obj_url = obj.url
    #
    # obj = WirrURL.objects.get(shortcode=shortcode)
    # return HttpResponse("hello {sc}".format(sc=obj_url))

class wirrcbview(View):
    def get(self,request,shortcode=None,*args,**kwargs):
        obj = get_object_or_404(WirrURL, shortcode=shortcode)

        return HttpResponseRedirect(obj.url)

    def post(self,request,*args,**kwargs):
        return HttpResponse ()

