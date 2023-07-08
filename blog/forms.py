from django import forms
from .models import BlogPostModels

class BlogPostForm(forms.Form):
    titleForm = forms.CharField()
    slugForm = forms.SlugField()
    contentForm = forms.CharField(widget=forms.Textarea)

class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPostModels
        fields = ['titleModels', 'slugModels', 'contentModels']

    def clean_titleModels(self, *args, **kwargs):
        instance = self.instance
        titleModels = self.cleaned_data.get('titleModels')
        qs = BlogPostModels.objects.filter(titleModels__iexact=titleModels)
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("Please use another title. This one has already been used")
        return titleModels
