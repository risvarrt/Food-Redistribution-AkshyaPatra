from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

class Slider(models.Model):
    slider_image = models.ImageField(default='default.jpg', upload_to='slider')
    slider_short = models.CharField(null=True,max_length=30,blank=True)

class Post(models.Model):    
    STATUS_CHOICES = (
        ('Veg', 'Veg'),
        ('Non-Veg', 'Non-Veg'),
        ('Veg/Nonveg', 'Veg/Nonveg'),
    )
    type_of_food = models.CharField(max_length=20,choices=STATUS_CHOICES,default='Veg',blank=True, null=True)
    
    title = models.CharField(max_length=100,blank=True, null=True)
    address = models.CharField(max_length=100,blank=True, null=True)
    detail = models.FileField(upload_to='musics/',blank=True, null=True)
    date=models.DateField(auto_now=False, auto_now_add=False,blank=True, null=True)
    expire_time=models.TimeField(auto_now=False, auto_now_add=False,blank=True, null=True)
    availble_quantity_of_food=models.CharField(max_length=100,blank=True, null=True)
    image_of_food = models.ImageField(default=None, upload_to='profile_pics',blank=True, null=True)
    contact_no=models.IntegerField(blank=True, null=True)
    details_audio=models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    latitude = models.CharField(null=True,max_length=100,blank=True)
    longitude = models.CharField(null=True,max_length=100,blank=True)
    MSlug=models.SlugField(max_length=50,unique=True,blank=True)
    def save(self, *args, **kwargs):
        self.MSlug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    
    
class Comment(models.Model):
    Meeting_Comment=models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments',blank=True, null=True)
    Name=models.CharField(max_length=50, null=True)
    Body=models.TextField(null=True,blank=True)
    Required_Quantity=models.IntegerField(blank=True, null=True)
    Active=models.BooleanField(default=True)
    comment_act=models.BooleanField(default=False)
    Created=models.DateTimeField(auto_now_add=True)
    Parent=models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='replies')

    class Meta:
        ordering = ('-Created',)

    def __str__(self):
        return 'Comment By {}'.format(self.Name)

class Feedback(models.Model):
    Name = models.CharField(null=True,max_length=100)
    Content = models.TextField()   

class Meeting(models.Model):
    Name = models.CharField(null=True,max_length=100)
    Content = models.TextField() 
    image = models.ImageField(default='default.jpg', upload_to='slider',blank=True, null=True)
    date=models.DateTimeField(null=True,auto_now=False, auto_now_add=False,blank=True)
    