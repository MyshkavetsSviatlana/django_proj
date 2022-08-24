from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from . import views
from Teacher.models import Teacher
from User.models import User


class TestTeacher(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = get_user_model().objects.create_user(
            email='test@email.com',
            password='Password1234',
            role='Super Admin'
        )
        self.user.save()
        self.teacher = Teacher.objects.create(
            surname='Зубрицкий',
            name='Александр',
            specialization='Питон',
            course_name='Python',
            url='1',
        )

    def test_list_teacher(self):
        request = self.factory.get('/api/v1/teachers/')
        request.user = self.user
        response = views.TeacherListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Александр')

    def test_detail_teacher(self):
        request = self.factory.get('/api/v1/teachers/')
        request.user = self.user
        response = views.TeacherDetailsView.as_view()(request, pk=1)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Питон')

    def test_create_teacher(self):
        request = self.factory.post('/api/v1/teachers/new/', {
            "pk": 2,
            "surname": 'Тестовое',
            "name": 'Создание',
            "specialization": 'Питон',
            "course_name": 'Основы разработки сайтов',
            "url": '2'
        })
        request.user = self.user
        response = views.TeacherCreateView.as_view()(request)
        response.render()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Teacher.objects.count(), 2)

    def test_teacher_update_view(self):
        request = self.factory.put('/api/v1/teachers/edit/', {
            "surname": 'Тестовое',
            "name": 'Изменение',
            "specialization": 'Сайт',
        })
        request.user = self.user
        response = views.TeacherUpdateView.as_view()(request, pk=2)
        self.assertEqual(response.status_code, 200)
        self.teacher.refresh_from_db()
        self.assertEqual(self.teacher.specialization, 'Сайт')
        self.assertEqual(self.teacher.surname, 'Тестовое')
    #
    # # def test_teacher_delete_view(self):
    #     self.client.login(email='test@email.com', password='Password1234')
    #     response = self.client.get(
    #         reverse('teacher_confirm_delete', args='1'))
    #     self.assertContains(response, 'Are you sure you want to delete')
    #     self.assertEqual(Teacher.objects.count(), 1)
