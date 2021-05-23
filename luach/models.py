from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

# date details
class MyDate(models.Model):
    english_date = models.DateField(auto_now=False)
    hebrew_date = models.CharField(max_length=20,unique=False)
    hebrew_year = models.CharField(max_length=10,unique=False)
    sof_zman_1 = models.TimeField(auto_now=False,blank=True,null=True)
    sof_zman_2 = models.TimeField(auto_now=False,blank=True,null=True)
    sof_zman_tefila = models.TimeField(auto_now=False,blank=True,null=True)
    
    def get_absolute_url(self ):
        return reverse('date_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return ('%s %s' % (self.hebrew_date,self.hebrew_year))


# images
class Images(models.Model):
    image = models.ImageField(unique=False,upload_to='images/')

    def get_absolute_url(self):
        return reverse("image_detail",kwargs={'pk':pk})

    def __str__(self):
        return self.image.name
    



#mazel
class MazelTov(models.Model):
    date = models.ForeignKey('luach.MyDate',related_name='mazel',on_delete=models.CASCADE)
    mazel_tov = models.TextField(max_length=400)

    def get_absolute_url(self):
        return reverse("date_detail",kwargs={'pk':self.date.pk})

    def __str__(self):
        return str(self.mazel_tov)

#connect days and images together
class DayImage(models.Model):
    date = models.ForeignKey('luach.MyDate',related_name='day',on_delete=models.CASCADE)
    images = models.ForeignKey('luach.Images',related_name='images',on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse("dayimage_detail",kwargs={'pk':self.pk})



class Message(models.Model):
    message = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return self.message

class Add(models.Model):
    ad_image = models.ImageField(unique=False,upload_to='images/')

    def __str__(self):
        return self.ad_image.name
    
