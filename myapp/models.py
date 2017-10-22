from django.db import models

# Create your models here.
class Scenery(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	typeId = models.IntegerField()
	typeCode = models.CharField(max_length=7)
	lat = models.FloatField()
	lng = models.FloatField()
	rank = models.IntegerField()
	description = models.TextField()
	attraction = models.CharField(max_length=255)
	img = models.CharField(max_length=255)
	imgPlaceHolder = models.CharField(max_length=255)
	parentId = models.IntegerField()
	city = models.ForeignKey(
		'City',
		on_delete = models.CASCADE,
	)

	def __unicode__(self):
		return self.name + self.attraction

class City(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=255)
	lat = models.FloatField(default=0)
	lng = models.FloatField(default=0)
	rank = models.IntegerField(default=0)
	description = models.TextField()
	attraction = models.CharField(max_length=255)
	img = models.CharField(max_length=255)
	imgPlaceHolder = models.CharField(max_length=255)

	def __unicode__(self):
		return self.name
