from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from courses.models import Course
from courses.pagination import CoursePagination
from courses.permissions import IsModeratorPermission, IsSuperUserPermission
from courses.serializers.course import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    # если тестируем
    # permission_classes = [AllowAny]
    # queryset = Course.objects.all()

    # если НЕ тестируем
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return Course.objects.all()
        # if self.request.user.is_superuser:
        #     return Course.objects.all()
        return Course.objects.filter(owner=self.request.user)

    default_permission_class = [IsAuthenticated()]
    permissions = {
        'create': [IsSuperUserPermission()],
        'list': [IsAuthenticated() or IsModeratorPermission() or IsSuperUserPermission()],
        'retrieve': [IsAuthenticated() or IsModeratorPermission() or IsSuperUserPermission()],
        'update': [IsAuthenticated() or IsModeratorPermission() or IsSuperUserPermission()],
        'partial_update': [IsAuthenticated() or IsModeratorPermission() or IsSuperUserPermission()],
        'destroy': [IsSuperUserPermission()],

    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission_class)

    def perform_create(self, serializer):
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()
