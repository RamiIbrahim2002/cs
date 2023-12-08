from django import forms

class new_article_form(forms.Form):
    article_title = forms.CharField(label="Article title")
    article_content = forms.CharField(
        label="Article content",
        widget=forms.Textarea()
    )