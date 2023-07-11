from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPostModels(models.Model): #blogpostmodels_set() -> query set
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    titleModels = models.CharField(max_length=100)
    contentModels = models.TextField(null=True, blank=True)
    slugModels = models.SlugField(unique=True)
    publushed_dateME = models.DateTimeField(auto_now=False, auto_now_add=False)
    timestampMe = models.DateTimeField(auto_now_add=True)
    updatedMe = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-publushed_dateME", "-timestampMe", "-updatedMe"]


    def get_absolute_url(self):
        return f"/blogs/{self.slugModels}/"
    
    def get_edit_url(self):
        return f"{self.get_absolute_url()}edit/"
    
    def get_delete_url(self):
        return f"{self.get_absolute_url()}delete/"
    
    

  