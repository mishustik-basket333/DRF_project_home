from rest_framework import serializers

from courses.models import Course, Lesson
from courses.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(read_only=True, many=True)

    # lesson = serializers.SerializerMethodField()
    # def get_lesson(self, obj):
    #     return Lesson.objects.filter(course=obj.pk)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    class Meta:
        model = Course
        fields = '__all__'
        # fields = ("id", 'name', 'pict', 'description', 'lesson_count', 'lalala', )
