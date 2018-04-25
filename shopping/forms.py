from django import forms


class ReviewForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea())
    stars = forms.IntegerField(max_value=5, min_value=1)