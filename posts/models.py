from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save

from django.utils.text import slugify

# Create your models here.

def upload_location(instance,filename):
	return "%s/%s"%(instance.id,filename)

class Post(models.Model):
	title = models.CharField(max_length=200) #username
	project_url = models.CharField(max_length=200, default=' ')
	sourceCode_url = models.CharField(max_length=200, default=' ')
	# image = models.FileField(null=True, blank=True)
	# slug = models.SlugField(unique=True)

	image = models.ImageField(upload_to=upload_location,
		null=True, blank=True, 
		width_field="width_field", 
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field=models.IntegerField(default=0)
	content = models.TextField(max_length=200)
	updated = models.DateTimeField(auto_now=True, auto_now_add = False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add = True)

#
	def __unicode__(self):
		return self.title

# get absolute url

	def get_absolute_url(self):
		 return reverse("posts:detail", kwargs={"id": self.id})
		# return "posts/%s/"%(self.id)
	
	#handles post order
	class Meta:
		ordering = ["-id","-timestamp","-updated"]



#could not get slug to work :(s
#recursive function to check if slug created

# def create_slug(instance, new_slug=None):
# 	slug = slugify(instance.title)
# 	if new_slug is not None:
# 		slug = new_slug
# 	qs= Post.objects.filter(slug=slug).order_by("-id")
# 	exists = qs.exists()
# 	if exists:
# 		new_slug= "%s-%s" %(slug, qs.first().id)
# 		return create_slug(instance, new_slug=new_slug)
# 	return slug

# def pre_save_post_receiver(sender, instance, *args, **kwargs):
# 	if not instance.slug:
# 		instance.slug = create_slug(instance)


# pre_save.connect(pre_save_post_receiver,sender=Post)