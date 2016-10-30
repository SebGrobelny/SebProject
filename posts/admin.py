from django.contrib import admin

# Register your models here.
from .models import Post 

class PostAdmin(admin.ModelAdmin):
	# setting what model admin will use
	list_display = ["__unicode__","updated","timestamp"]
	search_fields = ["title","content"]
	
	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)