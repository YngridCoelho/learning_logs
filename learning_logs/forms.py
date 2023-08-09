from .models import Topic, Entry
from django import forms


class TopicForm(forms.ModelForm):
    class Meta:
        text = forms.CharField(error_messages={'requered': 'erro'})
        model = Topic
        fields = ['text']
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        widget = {'text': forms.Textarea(attrs={'cols':80})}

        