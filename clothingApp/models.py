from django.db import models

# Create your models here.


class ProductDetail(models.Model):

  product_image = models.URLField(blank=True , null=True) 
  buy_now_link = models.URLField(blank=True , null=True)
  product_name = models.CharField(max_length=200)
  product_prize = models.CharField(max_length=100)
  def __str__(self):

    return self.product_name


class One_Time(models.Model):

    View_All_products = models.URLField( blank=True , null=True)
    shop_now = models.URLField(blank=True , null=True)
    products = models.URLField( blank=True , null=True)
    Front_pic = models.URLField(blank=True , null=True)
    contact = models.URLField(blank=True , null=True)
    about = models.URLField(blank=True , null=True)

class SocialMedia(models.Model):

	instagram = models.URLField(blank=True , null=True)
	youtube = models.URLField(blank=True , null=True)
	twitter = models.URLField(blank=True , null=True)
	first = models.URLField(blank=True , null=True)
	second = models.URLField(blank=True , null=True)





