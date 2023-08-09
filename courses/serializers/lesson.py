from rest_framework import serializers

from courses.models import Lesson, Course
from courses.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            UrlValidator(field='video_url')
        ]
