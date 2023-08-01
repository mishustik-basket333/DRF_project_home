from rest_framework import serializers

from courses.models import Lesson, Course


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
