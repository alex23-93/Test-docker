from django.forms import ModelForm, widgets
from django import forms
from projects.models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_images', 'description', 'demo_link', 'source_link', 'tags']

        # Улучшаем строку выбора тегов

        widgets = {'tags': forms.CheckboxSelectMultiple()}

    # Улучшаем поля ввода
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

    labels = {
        'value': 'Place your vote',
        'body': 'Add a comment with your vote'
    }
    
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})