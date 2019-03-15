from django import forms
from django.contrib.auth.models import User
from web_app.models import UserProfile, Post, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phoneNumber', 'location', 'photo')


class PostForm(forms.ModelForm):
    # date = forms.DateTimeField(
    #     input_formats=['%d/%m/%Y %H:%M'],
    #     widget=forms.DateTimeInput(attrs={
    #         'class': 'form-control datetimepicker-input',
    #         'data-target': '#datetimepicker1'
    #     })
    # )
    CHOICES = [
        ('1', 'Found'),
        ('2', 'Lost'),
    ]

    status = forms.CharField(label='Post Type', widget=forms.Select(choices=CHOICES))
    
    title = forms.CharField(
        max_length=65,
        label='Post Title'
        # widget=forms.Textarea(attrs={'placeholder': 'Title'})
    )

    text = forms.CharField(
        max_length=2000,
        label='Description',
        widget=forms.Textarea(attrs={'placeholder': 'Write your description here...', 'class': 'full-width'})
    )

    location = forms.CharField(
        max_length=250,
        label='Location'
    )

    class Meta:
        model = Post
        fields = ('status', 'title', 'location', 'text', 'image')

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        # exclude = ('category',)


class CommentForm(forms.ModelForm):

    text = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'placeholder': 'Your Message*', 'class': 'full-width'}),
    )

    class Meta:
        model = Comment
        fields = ('text', )

# class EditProfileForm(forms.ModelForm):

#     template_name='/something/else'

#     class Meta:
#         model = UserProfile
#         fields = (
#             'phoneNumber',
#             'location'
#         )