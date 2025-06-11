from django.db import models
from django.utils.text import slugify


class Project(models.Model):

  class Status(models.TextChoices):
    PUBLISHED = 'PB', 'Published'
    DRAFT = 'DF', 'Draft'

  title = models.CharField(max_length=264)
  summary = models.CharField(max_length=255)
  description = models.CharField(max_length=500)
  image = models.ImageField(upload_to='uploads/')
  address = models.URLField()
  status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
  slug = models.SlugField(unique=True, blank=True)
  meta_title = models.CharField(max_length=70, blank=True)
  meta_description = models.CharField(max_length=160, blank=True)

def save(self, *args, **kwargs):
  if not self.slug:
    self.slug = slugify(self.title)

  if not self.meta_title:
    self.meta_title = self.title[:70]

  if not self.meta_description:
    self.meta_description = (self.summary or self.description)[:160]

    super().save(*args, **kwargs)


  def __str__(self):
    return self.title