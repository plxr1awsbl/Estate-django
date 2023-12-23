import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Property(models.Model):

    identifier = models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=50)
    main_photo = models.ImageField(blank= True, null=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    
    sq_mt = models.PositiveSmallIntegerField(null=True, blank=True)
    floors = models.PositiveSmallIntegerField(default=1)
    bedrooms = models.PositiveSmallIntegerField(default=2)
    bathrooms = models.PositiveSmallIntegerField(default=2)
    
    description = models.TextField(null=True, blank=True)
    project = models.CharField(max_length=20, help_text="Project that owns the property", default=None, null=True)
    
    
    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("details", kwargs={"prop_slug": self.slug})


class PropertyImage(models.Model):
    prop = models.ForeignKey(Property, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()
    description = models.CharField(max_length=15, null=True, blank=True)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
     
        
class PropertyBenefit(models.Model):
    title = models.CharField(max_length=20)
    prop = models.ForeignKey(Property, related_name='benefits', on_delete=models.CASCADE)