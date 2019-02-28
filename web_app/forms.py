from django import forms
from django.contrib.auth.models import User
from web_app.models import UserProfile, Post, Comment

# class CategoryForm(forms.ModelForm):
#     name = forms.CharField(max_length=128,
#                            help_text="Please enter the category name.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
#     slug = forms.CharField(widget=forms.HiddenInput(), required=False)

#     # An inline class to provide additional information on the form.
#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = Category
#         fields = ('name',)

#     def clean(self):
#         cleaned_data = self.cleaned_data
#         url = cleaned_data.get('url')

#         # If url is not empty and doesn't start with 'http://',
#         # then prepend 'http://'.
#         if url and not url.startswith('http://'):
#             url = 'http://' + url
#         cleaned_data['url'] = url
#         return cleaned_data


# class PageForm(forms.ModelForm):
#     title = forms.CharField(max_length=128,
#                             help_text="Please enter the title of the page.")
#     url = forms.URLField(max_length=200,
#                          help_text="Please enter the URL of the page.")
#     views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model = Page

#         # What fields do we want to include in our form?
#         # This way we don't need every field in the model present.
#         # Some fields may allow NULL values, so we may not want to include them.
#         # Here, we are hiding the foreign key.
#         # we can either exclude the category field from the form,
#         exclude = ('category',)
#         # or specify the fields to include (i.e. not include the category field)
#         # fields = ('title', 'url', 'views')

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
    
    title = forms.CharField(
        max_length=65,
        # widget=forms.Textarea(attrs={'style': 'border-color: red;'})
    )

    text = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(attrs={'style': 'border-color: orange;'})
    )
    class Meta:
        model = Post
        fields = ('title', 'text', 'image')

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        # exclude = ('category',)


class CommentForm(forms.ModelForm):

    text = forms.CharField(
        max_length=2000,
        widget=forms.Textarea()
    )

    class Meta:
        model = Comment
        fields = ('text', )
