from django import forms

class ResumeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    skills = forms.CharField(widget=forms.Textarea)  # For simplicity, assuming skills are entered as text
    experience = forms.CharField(widget=forms.Textarea)  # Same for experience
    education = forms.CharField(widget=forms.Textarea)  # Same for education
    awards = forms.CharField(widget=forms.Textarea)  # Same for awards
    references = forms.CharField(widget=forms.Textarea)  # Same for references
    about_me = forms.CharField(widget=forms.Textarea)  # About me section
