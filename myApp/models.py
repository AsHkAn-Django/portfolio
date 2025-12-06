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
  status = models.CharField(
    max_length=2,
    choices=Status.choices,
    default=Status.DRAFT
  )
  slug = models.SlugField(unique=True, blank=True)
  meta_title = models.CharField(max_length=70, blank=True)
  meta_description = models.CharField(max_length=160, blank=True)

  # new fields
  github_link = models.URLField(
    blank=True,
    null=True,
    verbose_name="Github Repository URL",
    help_text="Link to the source code repository"
  )
  tech_stack = models.CharField(
    max_length=255,
    blank=True,
    verbose_name="Technologies Used",
    help_text="Comma-seperated list (e.g., Python, Django, Nginx)"
  )
  priority_order = models.IntegerField(
    default=0,
    verbose_name="Display Priority",
    help_text="""Higher number means higher priority,
    projects with higher number will appear first."""
  )

def save(self, *args, **kwargs):
  if not self.slug:
    self.slug = slugify(self.title)

  if not self.meta_title:
    self.meta_title = self.title[:70]

  if not self.meta_description:
    description_source = self.summary or self.description
    self.meta_description = description_source[:160]

    super().save(*args, **kwargs)

  def __str__(self):
    return self.title

class Meta:
  # Sort first by priority_order 
  ordering = ['-priority_order', '-pk']
