from django import forms

class AudioForm(forms.Form):
    audio_file = forms.FileField()