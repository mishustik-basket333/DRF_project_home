from rest_framework import serializers

from courses.models import Course, Lesson, Subscription
from courses.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='course', many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    # def get_lessons_count(self, course):
    #     return Lesson.objects.filter(course=course).count()

    # lesson = serializers.SerializerMethodField()
    # def get_lesson(self, obj):
    #     return Lesson.objects.filter(course=obj.pk)

    def get_lesson_count(self, obj):
        return Lesson.objects.filter(course=obj.pk).count()

    def get_subscription(self, course):
        return Subscription.objects.filter(course=course).exists()

    class Meta:
        model = Course
        # fields = '__all__'
        fields = ("id", 'name', 'pict', 'description', 'lesson_count', 'lessons', 'subscription')
