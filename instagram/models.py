from django.db import models
import datetime as dt 

# Create your models here.
class Profile(models.Model):
    profile_photo = models.ImageField('instagram/', null = True)
    bio = models.TextField()

    def __str__(self):
        return self.profile

    def save_profile(self):
        self.save()

    def delete_profile(self):
        Profile.objects.all().delete()        
  


class Image(models.Model):
    image = models.ImageField('instagram/')
    image_name = models.CharField(max_length =30)
    image_caption = models.TextField()
    profile = models.ForeignKey(Profile)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()    

    def __str__(self):
        return self.image



class comments(models.Model):
    comments = models.CharField(null = True, blank=True, max_length= 5000)
    date = models.TextField(blank=True, null=True)
    image = models.ForeignKey(Image, null= True)

    def save_comments(self):
        self.save()

    def delete_comments(self):
        self.delete()
            


    # @classmethod
    # def search_by_image_category(cls,search_term):
    #     pictures = cls.objects.filter(image_name__icontains=search_term)
    #     return picturescomments
