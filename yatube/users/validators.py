from . import forms


def validate_not_empty(value):
    if value == '':
        raise forms.ValidationError(
            params={'value': value},
        )
