from .models import Image,Profile,Comments
from django import forms
#......
class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['pub_date','profile','user','comment','like']

class UpdatebioForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['comment_image','user']

