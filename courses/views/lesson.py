from rest_framework import generics

from courses.models import Lesson
from courses.pagination import LessonPagination
from courses.permissions import IsModeratorPermission, IsSuperUserPermission
from courses.serializers.lesson import LessonSerializer
from rest_framework.permissions import IsAuthenticated


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer

    permission_classes = [IsSuperUserPermission]


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = LessonPagination

    permission_classes = [IsAuthenticated | IsModeratorPermission | IsSuperUserPermission]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

    # queryset = Lesson.objects.all()

    #  Если в settings присутствует
    #  'DEFAULT_PERMISSION_CLASSES': [
    #      'rest_framework.permissions.AllowAny',
    #   ]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer

    permission_classes = [IsAuthenticated | IsModeratorPermission | IsSuperUserPermission]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

    # queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer

    permission_classes = [IsAuthenticated | IsModeratorPermission | IsSuperUserPermission]

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Lesson.objects.all()
        return Lesson.objects.filter(owner=self.request.user)

    # queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    permission_classes = [IsSuperUserPermission]
