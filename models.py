from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField


from django.db import models
from datetime import datetime

def get_current_date_time():
		return datetime.now()

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=50)
<<<<<<< HEAD
	slug = AutoSlugField(max_length=50, populate_from=('title'))
	projects = models.ManyToManyField("projects.Project", verbose_name="Related Projects", blank=True)
	tags = models.ManyToManyField("Tag")
	date_created = models.DateTimeField(primary_key=True, default=get_current_date_time, editable=False)
=======
	projects = models.ManyToManyField("projects.Project", verbose_name="Related Projects", blank=True)
	tags = models.ManyToManyField("Tag")
	date_created = models.DateTimeField(primary_key=True, default=get_current_date_time)
>>>>>>> 9004bf328deb9a9a4f46a19a888042c1dfcd492d
	last_modified = models.DateTimeField(auto_now=True)
	content = models.TextField()

	def __str__(self):
		return self.title

class Tag(models.Model):
	name = models.CharField(max_length=50, primary_key=True)
<<<<<<< HEAD
	slug = AutoSlugField(max_length=50, populate_from=('name'))

	def __str__(self):
		return self.name

	def popularity(self):
		return self.related.all()
=======

	def __str__(self):
		return self.name
>>>>>>> 9004bf328deb9a9a4f46a19a888042c1dfcd492d
