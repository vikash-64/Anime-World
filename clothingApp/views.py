from django.shortcuts import render
from . models import ProductDetail , One_Time , SocialMedia



def index(request):
    products = ProductDetail.objects.all().values()
    onetimes = One_Time.objects.all().values()
    socialmedias = SocialMedia.objects.all().values()
    
    context = {'onetimes':onetimes ,'products': products , 'socialmedia' : socialmedias }

    return render(request, 'index.html' , context )  
