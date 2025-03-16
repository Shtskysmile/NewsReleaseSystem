# article/forms.py
from django import forms
from .models import ArticleInfo, Category
from ckeditor.widgets import CKEditorWidget

class ArticleForm(forms.ModelForm):
    class Meta:
        model = ArticleInfo
        fields = ['title', 'desc', 'cover', 'category', 'content']

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['desc'].widget = forms.Textarea(attrs={'class': 'form-control'})
        self.fields['cover'].widget = forms.FileInput(attrs={'type': 'file'})
        self.fields['category'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['category'].queryset = Category.objects.all()
        self.fields['content'].widget = CKEditorWidget()