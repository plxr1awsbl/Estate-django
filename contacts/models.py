import uuid

from django.db import models
from django.urls import reverse

# Create your models here.
class Application(models.Model):

    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this Application")
    user_name = models.CharField(max_length=10)
    phone_num = models.CharField(max_length=12)
    description = models.CharField(max_length=300, null=True)
    
    
    class Meta:
        verbose_name = "Application"
        verbose_name_plural = "Applications"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Application_detail", kwargs={"pk": self.pk})
