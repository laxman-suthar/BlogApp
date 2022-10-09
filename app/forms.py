
from django import forms
from .models import Blog

class Blogform(forms.ModelForm):
    class Meta:
        model=Blog  
        widgets = {
            'blog_text': forms.Textarea(),
        }

        fields=["blog_title","blog_text"]

    def __init__(self, *args, **kwargs):
        super(Blogform, self).__init__(*args, **kwargs)
        self.fields['blog_title'].widget.attrs.update({'class': 'form-control'})
        self.fields['blog_text'].widget.attrs.update({'class': 'form-control'})
        self.fields["blog_text"].label="enter your text"
        



