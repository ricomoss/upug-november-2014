from django import forms


class FibNumForm(forms.Form):
    fib_index = forms.IntegerField(required=False)
