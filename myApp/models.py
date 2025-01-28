from django.db import models

class Project(models.Model):
  title = models.CharField(max_length=264)
  description = models.CharField(max_length=264)
  image = models.ImageField(upload_to='uploads/')
  address = models.URLField()

  def __str__(self):
    return self.title

