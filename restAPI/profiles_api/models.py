from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    PermissionsMixin, 
    BaseUserManager
    )

from django.conf import settings


class UserProfileManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password= None):
        if not email:
            raise ValueError('User must have an email address.')
        
        email= self.normalize_email(email)
        user= self.model(email= email, first_name= first_name, last_name= last_name)
        user.set_password(password)
        user.save(using= self._db)
        return user
    
    def create_superuser(self, email, first_name, last_name, password):
        user= self.create_user(email, first_name, last_name, password)
        user.is_superuser= True
        user.is_staff= True
        user.save(using= self._db)
        
     
class User(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(max_length= 255, unique= True)
    first_name= models.CharField(max_length= 255)
    last_name= models.CharField(max_length= 255)
    is_active= models.BooleanField(default= True)
    is_staff= models.BooleanField(default= False)
    
    objects= UserProfileManager()
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS= ['first_name', 'last_name']
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
    
    def get_first_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
    
    
    
class ProfileFeedItem(models.Model):
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, name='user_profile')
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add= True)
    
    def __str__(self):
        return self.status_text