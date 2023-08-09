from rest_framework import serializers


class UrlValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_data = value.get(self.field)
        if tmp_data is not None and tmp_data[12:23] != 'youtube.com':
            # if tmp_data[12:23] != 'youtube.com':
            raise serializers.ValidationError('URL должен ссылаться на youtube.com')
