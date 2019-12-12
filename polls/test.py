from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from . import apiviews

# ************Testing with APIRequestFactory*************

# Testing without authentication
class TestPoll(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.uri = '/polls/'

    def test_list(self):
        request = self.factory.get(self.uri)
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            f"Expected Response Code 200, received {response.status_code} instead"
        )


# Testing with authentication
class TestPoll(APITestCase):

    def setUp(self):
        self.factory = APIRequestFactory()
        self.uri = '/polls/'
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test',
            email='testuser@test.com',
            password='test'
        )

    def test_list(self):
        request = self.factory.get(
            self.uri,
            HTTP_AUTHORIZATON=f'Token {self.token.key}',
        )
        request.user = self.user
        response = self.view(request)
        self.assertEqual(
            response.status_code, 200,
            f'Expected Response Code 200, received {response.status_code} instead'
        )


# **************Testing with APIClient***************


# Testing without authentication
class TestPoll(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.uri = '/polls/'
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})

    def test_list2(self):
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code, 200,
            f"Expected Response Code 200, received {response.status_code} instead"
        )


# Testing with authentiation
class TestPoll(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.uri = '/polls/'
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.token = Token.objects.create(user=self.setup_user())
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test',
            email='testuser@test.com',
            password='test'
        )

    def test_list2(self):
        self.client.login(username='test', password='test')
        response = self.client.get(self.uri)
        self.assertEqual(
            response.status_code, 200,
            f"Expected Response Code 200, received {response.status_code} instead"
        )


# ***********Testing .post and create**************

class TestPoll(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.uri = '/polls/'
        self.view = apiviews.PollViewSet.as_view({'get': 'list'})
        self.token = Token.objects.create(user=self.setup_user())
        self.token.save()

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            username='test',
            email='testuser@test.com',
            password='test'
        )

    def test_create(self):
        self.client.login(username='test', password='test')
        params = {
            "question": "How you dey?",
            "created_by": 1
        }
        response = self.client.post(self.uri, params)
        self.assertEqual(
            response.status_code, 201,
            msg=f"Expected Response Code 201, received {response.status_code} instead"
        )
