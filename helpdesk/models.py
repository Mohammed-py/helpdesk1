from django.db import models
from django.contrib.auth.models import AbstractUser






class User (AbstractUser):
    pass

class UserProfile(models.Model):
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   def __str__(self):
     return self.user.username


class Agent(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
  def __str__(self):
    return self.user.email




# Create your models here.
#class Region(models.Model):
 #   name = models.CharField(max_length=15)
    
    #@property
    #def R(self):
        #return self.city_set.all()
    #    return self.city.objects.all

  #  def __str__(self):
   #   return self.name




class City(models.Model):
    name = models.CharField(max_length=15)
    Ma_region = models.ForeignKey("Ma_dis", on_delete=models.CASCADE)
    
    #Region = models.ForeignKey(Region, on_delete=models.CASCADE)
   
    def __str__(self):
      return self.name



# Table of Major of Dis
class Ma_dis(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    region  = models.CharField(max_length=15)

   

    def __str__(self):
      return f"{self.first_name}  "


########### Table of Sub of Dis
class Sub_dis(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    Ma_dis = models.ForeignKey("Ma_dis", on_delete=models.SET_NULL , blank=True, null= True)
    city = models.ForeignKey("City", on_delete=models.SET_NULL , blank=True, null= True)
   


    def __str__(self):
      return f"{self.first_name} {self.last_name}"



# Table of POS
class Pos(models.Model):
    pos_code = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=20)
    sim_num = models.IntegerField( null=True, blank=True)
    Sub_dis = models.ForeignKey("Sub_dis", on_delete=models.SET_NULL , blank=True, null= True)
    #agent = models.ForeignKey("Agent", on_delete=models.CASCADE, blank=True, null= True)

    def save(self, *args, **kwargs):
        city = Sub_dis.first_name
        super(Pos, self).save(*args, **kwargs)

    def __str__(self):
      return f"{self.pos_code} {self.Sub_dis.city} / {self.city} "
