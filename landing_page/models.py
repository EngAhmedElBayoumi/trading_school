from django.db import models
from users.models import CustomUser
from ckeditor.fields import RichTextField
# Create your models here.

class UserLandingPage(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100,verbose_name="Arabic title")
    description = models.TextField()
    description_ar = models.TextField(verbose_name="Arabic description")
    image = models.ImageField(upload_to='static/landing_page/image', null=True, blank=True)
    video = models.FileField(upload_to='static/landing_page/video', null=True, blank=True)
    pagename = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)




class MainSection(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100,verbose_name="Arabic title")
    
    description=models.TextField()
    description_ar=models.TextField(verbose_name="Arabic Description")
    image=models.ImageField(upload_to='static/landing_page/image', null=True, blank=True)
    
    def __str__(self):
        return str(self.title)
    
    
class CoursesSection(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100,verbose_name="Arabic title")
    description=models.TextField()
    description_ar=models.TextField(verbose_name="Arabic Description")
    image=models.ImageField(upload_to='static/landing_page/image', null=True, blank=True)
    
    def __str__(self):
        return str(self.title)
    
    
class BenfitsSection(models.Model):
    title=models.CharField(max_length=100)
    title_ar=models.CharField(max_length=100,verbose_name="Arabic title")
    description=models.TextField()
    description_ar=models.TextField(verbose_name="Arabic Description")
    
    
    def __str__(self):
        return str(self.title)
    
    
class Pricing(models.Model):
    plan=models.CharField(max_length=100,verbose_name="Plan Name")
    plan_ar=models.CharField(max_length=100,verbose_name="Arabic Plan name")
    
    price=models.FloatField()
    features=RichTextField()
    features_ar=RichTextField(verbose_name="Arabic Features")
    
    
    def __str__(self):
        return str(self.plan)
    
    
class MainLandingPage(models.Model):
    # One-to-Many relationship with MainSection
    main_section = models.ForeignKey(MainSection, on_delete=models.CASCADE, related_name='landing_pages')
    # Many-to-Many relationships
    courses_sections = models.ManyToManyField(CoursesSection, related_name='landing_pages')
    benefits_sections = models.ManyToManyField(BenfitsSection, related_name='landing_pages')
    benfits_image=models.ImageField(upload_to="static/landing_page/image",null=True,blank=True)
    pricing_plans = models.ManyToManyField(Pricing, related_name='landing_pages')
    
    def __str__(self):
        return f"Landing Page {self.id}"
    
    
    
class UserRequested(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=100)
    age=models.IntegerField()
    gender=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    notes=models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    
    def __str__(self):
        return str(self.name)