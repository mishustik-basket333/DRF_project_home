from rest_framework import generics

from courses.models import Lesson
from courses.pagination import LessonPagination
from courses.permissions import IsModeratorPermission, IsSuperUserPermission
from courses.serializers.lesson import LessonSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    # permission_classes = [IsSuperUserPermission]
    # если тестируем
    permission_classes = [AllowAny]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = LessonPagination
    # queryset = Lesson.objects.all()

    # permission_classes = [IsAuthenticated | IsModeratorPermission | IsSuperUserPermission]
    # если тестируем
    permission_classes = [AllowAny]

    #  Если в settings присутствует
    #  'DEFAULT_PERMISSION_CLASSES': [
    #      'rest_framework.permissions.AllowAny',
    #   ]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | IsModeratorPermission | IsSuperUserPermission]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    # queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated | IsModeratorPermission | IsSuperUserPermission]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsSuperUserPermission]



