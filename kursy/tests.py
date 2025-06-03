from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from kursy.models import Kurs, Autor


class KursyApiTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.autor = Autor.objects.create(user=self.user)
        self.kurs = Kurs.objects.create(nazwa='Testowy Kurs', autor=self.autor)

        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_kursy_list(self):
        response = self.client.get('/api/kursy/')
        self.assertEqual(response.status_code, 200)

    def test_kurs_str(self):
        self.assertEqual(str(self.kurs), 'Testowy Kurs')

    def test_kurs_autor(self):
        self.assertEqual(self.kurs.autor.user.username, 'testuser')