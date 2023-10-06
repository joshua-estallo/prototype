from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class Dataset(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField()
  tags = models.TextField()
  overview = models.TextField(blank=True)
  file = models.FileField(upload_to="uploads/", 
                          validators=[FileExtensionValidator(allowed_extensions=["zip", "rar"])], blank=True)

  def __str__(self):
    return self.title