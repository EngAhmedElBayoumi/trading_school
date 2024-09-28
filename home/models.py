from django.db import models

# Create your models here.

class wellcome_message(models.Model):
    message=models.CharField(max_length=100 , verbose_name="English message")
    message_ar=models.CharField(max_length=100 , verbose_name="Arabic message")

    def __str__(self):
        return self.message
    