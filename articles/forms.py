from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        qs = Article.objects.all().filter(title__icontains=title)
        # print(qs, title, cleaned_data)
        if qs.exists():
            self.add_error('title', f'\"{title}\" is already in use.')
        return cleaned_data

class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == 'using forms':
    #         raise forms.ValidationError('This title is taken.')
    #     return title

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == 'using forms':
            self.add_error('title', 'This title is taken.')
        if "forms" in content or "forms" in title.lower():
            self.add_error('content', "forms cannot be in content")
            raise forms.ValidationError("forms is not allowed")
        return cleaned_data