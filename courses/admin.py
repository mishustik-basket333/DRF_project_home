from django.contrib import admin

from courses.models import Lesson, Course, Payment


# Register your models here.

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course",)
    list_filter = ("name",)
    search_fields = ("name", "course",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name",)
    list_filter = ("name",)
    search_fields = ("name",)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "course", "lesson")
    list_filter = ("user",)
    search_fields = ("user", "course", "lesson")

