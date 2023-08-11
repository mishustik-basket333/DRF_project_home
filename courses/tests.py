from rest_framework import status
from rest_framework.test import APITestCase

from courses.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):
    """Тест уроков"""

    def setUp(self) -> None:
        """Создание тестового урока"""

        self.lesson = Lesson.objects.create(name="test")
        self.user = User.objects.create(email='test@example.com', password='test', is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_1_create_lesson(self):
        """Тестирование создания урока """

        data = {
            'name': 'test1',
        }
        response = self.client.post('/courses/lesson/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_2_list_lesson(self):
        """Тестирование вывода списка уроков """

        Lesson.objects.create(name="test1")
        response = self.client.get('/courses/lesson/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Lesson.objects.all().count(), 2)

    def test_3_retrieve_lesson(self):
        """Тестирование вывода одного урока """

        response = self.client.get(f'/courses/lesson/{self.lesson.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.lesson.pk, 'course': None, 'name': 'test', 'description': None, 'preview': None,
             'video_url': None, 'owner': None}
        )

    def test_4_update_put_lesson(self):
        """"Тестирование put обновление урока"""

        data = {
            'name': 'test4',
            'description': 'any',
        }
        response = self.client.put(f'/courses/lesson/update/{self.lesson.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.lesson.pk, 'course': None, 'name': 'test4', 'description': 'any', 'preview': None,
             'video_url': None, 'owner': None}
        )

    def test_5_update_patch_lesson(self):
        """"Тестирование patch обновление урока"""

        data = {
            'name': 'test4',
            'description': 'any',
        }
        response = self.client.patch(f'/courses/lesson/update/{self.lesson.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.lesson.pk, 'course': None, 'name': 'test4', 'description': 'any', 'preview': None,
             'video_url': None, 'owner': None}
        )

    def test_6_destroy_lesson(self):
        """Тестирование удаления урока """

        response = self.client.delete(f'/courses/lesson/delete/{self.lesson.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Lesson.objects.all().exists())
        self.assertEqual(Lesson.objects.all().count(), 0)


class CourseTestCase(APITestCase):
    """Тест курсов"""

    def setUp(self) -> None:
        """Создание тестового курса"""

        self.course = Course.objects.create(name="test")
        self.user = User.objects.create(email='test@example.com', password='test', is_superuser=True, is_staff=True)
        self.client.force_authenticate(user=self.user)

    def test_1_create_course(self):
        """Тестирование создания курса """

        data = {
            'name': 'test1',
        }
        response = self.client.post('/courses/courses/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_2_list_course(self):
        """Тестирование списка курсов"""

        Course.objects.create(name="test2")
        response = self.client.get('/courses/courses/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Course.objects.all().count(), 2)

    def test_3_retrieve_course(self):
        """Тестирование вывода одного курса """

        response = self.client.get(f'/courses/courses/{self.course.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.course.pk, 'name': 'test', 'pict': None, 'description': None,
             "lesson_count": 0, 'lessons': [], 'subscription': False}
        )

    def test_4_update_put_course(self):
        """"Тестирование put обновление урока"""

        data = {
            'name': 'test4',
            'description': 'any',
        }
        response = self.client.put(f'/courses/courses/{self.course.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.course.pk, 'name': 'test4', 'pict': None, 'description': 'any',
             "lesson_count": 0, 'lessons': [], 'subscription': False}
        )

    def test_5_update_patch_course(self):
        """"Тестирование patch обновление урока"""

        data = {
            'name': 'test4',
            'description': 'any',
        }
        response = self.client.patch(f'/courses/courses/{self.course.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'id': self.course.pk, 'name': 'test4', 'pict': None, 'description': 'any',
             "lesson_count": 0, 'lessons': [], 'subscription': False}
        )

    def test_6_destroy_course(self):
        """Тестирование удаления урока """

        response = self.client.delete(f'/courses/courses/{self.course.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Course.objects.all().exists())
        self.assertEqual(Course.objects.all().count(), 0)
