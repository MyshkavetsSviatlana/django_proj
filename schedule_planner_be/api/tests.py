from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.test import APIRequestFactory

from api.subwaystation.views import SubwayStationViewSet
from schedule.models import SubwayStation


class TestSubwayStationList(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = SubwayStationViewSet.as_view({'get': 'list'})
        self.uri = ''

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'
                         .format(response.status_code))


# class TestSubwayStationPost(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.factory = APIRequestFactory()
#         self.view = SubwayStationViewSet.as_view({'post': 'create'})
#         self.user = self.setup_user()
#         self.token = Token.objects.create(user=self.user)
#         self.token.save()
#
#     @staticmethod
#     def setup_user():
#         User = get_user_model()
#         return User.objects.create_user(
#             email='testuser@test.com',
#             password='Test1234')
#
#     def test_create(self):
#         self.client.login(email='testuser@test.com',
#                           password='Test1234')
#         url = '/subwaystations/'
#         params = {
#             "station": "Test",
#         }
#         request = self.factory.post(url, params)
#         response = self.view(request)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(SubwayStation.objects.count(), 1)
#         self.assertEqual(SubwayStation.objects.get().station, "Test")
# class SubwayStationTestsPost(APITestCase):
#     """
#     Ensure we can create a new subwaystation object.
#     """
#
#     def setUp(self):
#         self.user = User.objects.create_user(email="test@gmail.com", password="Test1234", role="Super Admin")
#         self.client.force_authenticate(self.user)
#
#     def test_create_subwaystation(self):
#         url = "/api/v1/subwaystations/"
#         data = {
#             'station': 'Test station',
#         }
#         response = self.client.post(url, data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
