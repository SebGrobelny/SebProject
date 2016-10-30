from django import forms


from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = [
			"title",
			"project_url",
			"sourceCode_url",
			"image",
			"content"

		]
