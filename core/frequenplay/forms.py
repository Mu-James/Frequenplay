from django import forms
from .models import MultipleChoiceGame, Choice

class ChooseChoice(forms.Form):
    def __init__(self, MCG, *args, **kwargs ):
        self.MCG_choice_list = [(str(c.timestamp), str(c.timestamp)) for c in Choice.objects.filter(game=MCG)]
        super(ChooseChoice, self).__init__(*args, **kwargs)
        self.fields["Choices"] = forms.ChoiceField(choices=self.MCG_choice_list, widget=forms.RadioSelect)