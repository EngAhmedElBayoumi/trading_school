from django.db import models
from django.core.files.storage import FileSystemStorage
from moviepy.editor import VideoFileClip
#import MemberShip from accounts
from accounts.models import MemberShip
from users.models import CustomUser

# Create your models here.

#courses image title rate 
class Course(models.Model):
    member_ship = models.ForeignKey(MemberShip,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/course/image')
    title = models.CharField(max_length=100)
    number=models.IntegerField(default=1)
    rate = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['id']
    
    
    def __str__(self):
        return self.title
    
#course lecture title image description video url rate number duration
class Lecture(models.Model):
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/course/image')
    description = models.TextField(null=True , blank=True)
    video = models.FileField(upload_to='static/course/video')
    number = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['id']
        
        
    def __str__(self):
        return self.title

    
class Lecture_rate(models.Model):
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    lecture=models.ForeignKey(Lecture,on_delete=models.CASCADE)
    star= models.IntegerField(default=0)

#viewlecture
class ViewLecture(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture,on_delete=models.CASCADE)
    time = models.IntegerField(default=0)
    #create at
    create_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user) 

#viewcourse
class ViewCourse(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    time = models.IntegerField(default=0)
    def __str__(self):
        return str(self.time)
    
    
    
# class CourseRating(models.Model):
#     course = models.OneToOneField(Course, on_delete=models.CASCADE)
#     rating = models.FloatField(default=0)
    
#     def __str__(self):
#         return str(self.rating)

    

