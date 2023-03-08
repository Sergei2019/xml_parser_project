from django import forms


class UploadFiles(forms.Form):
    docfile = forms.FileField(
        label = 'Выбрать файл',
        widget = forms.ClearableFileInput(attrs={'multiple': True}),
    )