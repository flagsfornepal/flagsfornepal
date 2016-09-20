from django import forms

class FlagForm(forms.Form):
    image = forms.ImageField(label="Select a picture for your flag", required=False)
    tagline = forms.CharField(label="Short tagline", max_length=50, required=False)
    name = forms.CharField(label="Your name", max_length=50, required=False)
    location = forms.CharField(label="Your location", max_length=50, required=False)
    email = forms.EmailField(label="Email", max_length = 50, required=False)
