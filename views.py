from rest_framework.exceptions import ValidationError

def validate(self, data):
    if not data['title']:
        raise ValidationError("Title is required")
    return data
