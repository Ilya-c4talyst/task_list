from django import forms
from .models import Task, Category

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'author', 'category', 'description', 'deadline']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'slug']
