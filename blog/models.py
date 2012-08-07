from django.db import models
from tinymce.models import HTMLField

CATEGORY = (
	('ACT', 'Activities'),
	('ACH', 'Achievements'),
	)

class Article(models.Model):
	date = models.DateField()
	title = models.CharField(max_length=127)
	category = models.CharField(max_length=15, choices=CATEGORY)
	preview = HTMLField()
	content = HTMLField()
	
	def __unicode__(self):
		return u'%s %s' % (self.category, self.title)

