from django import forms


from .models import Post
from django.contrib.auth.models import User

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
class UserForm(forms.ModelForm):

		password = forms.CharField()
		class Meta:
			model = User
			fields = ['username', 'email','password']