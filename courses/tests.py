from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
#     """Тест уроков"""
    def setUp(self) -> None:
        """"""
#         self.name = "lalala"
#         self.video_url = '/courses/'
        # self.course = Course.objects.create(name='test')
        # self.user = User.objects.create(email='test@lalala.com', password='123test')
        # self.data = {
        #     'course': self.course,
        #     'lesson_name': 'test',
        #     'owner': self.user
        # }
        #
        # self.lesson = Lesson.objects.create(**self.data)
        # self.client.force_authenticate(user=self.user)

    # def test_1_create_lesson(self):
    #     """Тестирование создания урока """
    #     data = {
    #         'course': self.course,
    #         'lesson_name': 'test2',
    #         'owner': self.user.pk
    #     }
    #     response = self.client.post(f'{self.url}lesson/create/', data=data)
    #
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #
    #     self.assertEqual(Lesson.objects.all().count(), 2)



    def test_2_list_lesson(self):
        """Lesson list testing """
        Lesson.objects.create(name="lalala")
        response = self.client.get('courses/lesson/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)




# class CourseTestCase(APITestCase):
#     """Тест курсов"""
#
#     def setUp(self) -> None:
#         """Тестовый образец"""
#         pass
#
#
#     def test_2_list_lesson(self):
#         """Lesson list testing """
#
#         Course.objects.create(name="lalala")
#         response = self.client.get('/courses/courses/')
#
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

