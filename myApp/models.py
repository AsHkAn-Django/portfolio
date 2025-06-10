from django.db import models

class Project(models.Model):

  class Status(models.TextChoices):
    PUBLISHED = 'PB', 'Published'
    DRAFT = 'DF', 'Draft'

  title = models.CharField(max_length=264)
  description = models.CharField(max_length=264)
  image = models.ImageField(upload_to='uploads/')
  address = models.URLField()
  status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

  def __str__(self):
    return self.title