from django import forms
class Search(forms.Form):
    search = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={'placeholder': 'Search', 'class': 'search', 'autocomplete': 'off',
            'style': 'height:35px; font-size:15pt;'
        })
        )