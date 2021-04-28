from django import forms
from .models import Profile,Projects,Rates,Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ('title','image_landing','description', 'link')
        
        
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio','website') 
        
class VotesForm(forms.ModelForm):
    class Meta:
        model = Rates
        fields = ('design','usability','content')
        
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)