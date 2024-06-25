from django import forms
from .models import Post,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'categories', 'tags']  # Assuming categories and tags are many-to-many fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom initialization if needed
        self.fields['categories'].widget.attrs.update({'class': 'form-control', 'multiple': True})
        self.fields['tags'].widget.attrs.update({'class': 'form-control', 'multiple': True})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add custom initialization if needed
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows': 3})
