from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from . import views


class TestTeacher(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.TeacherListView.as_view()
        self.uri = '/api/v1/teachers/'

    def test_list_teacher(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    # def test_detail_teacher(self):
    #
    #
    # def test_create_teacher(self):
    #     params = {
    #         "surname": 'Тестовое',
    #         "name": 'Создание',
    #         "specialization": 'Питон',
    #         "url": '1'
    #     }
    #     response = self.client.post()