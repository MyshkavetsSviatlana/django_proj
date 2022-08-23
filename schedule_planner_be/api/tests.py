from rest_framework import status
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
#         self.factory = APIRequestFactory()
#         self.view = SubwayStationViewSet.as_view({'post': 'create'})
#         self.uri = ''
#
#     def test_create(self):
#         params = {
#             "station": "Test station"
#         }
#         request = self.factory.post(self.uri, params)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 201,
#                          'Expected Response Code 201, received {0} instead.'
#                          .format(response.status_code))

class SubwayStationTestsPost(APITestCase):
    """
    Ensure we can create a new subwaystation object.
    """
    def setUp(self):
        self.client = APIClient()

    def test_create_subwaystation(self):
        url = ''
        data = {"station": "Test station"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SubwayStation.objects.count(), 1)
        self.assertEqual(SubwayStation.objects.get().station, 'Test station')
