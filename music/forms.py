from django import forms
from music.models import Song
from django.utils.text import slugify
class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields= ["name","singer","tags","image","audio"]

    def clean_name(self):
        data = self.cleaned_data["name"]
        if Song.objects.filter(slug = slugify(data)).exists() :
            raise forms.ValidationError ("there are Song with same Name")
        return data
    

