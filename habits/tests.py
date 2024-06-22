from datetime import timedelta
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habits
from users.models import User


class HabitsTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(email="igorskyeng@sky.pro")
        self.user.set_password("12345")
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habits.objects.create(
            user=self.user,
            place="Тренажерный зал",
            time="2024-06-22 22:26:00",
            action="Занятие на беговой дорожке",
            sign_pleasant_habit=False,
            related_habit=None,
            frequency="Раз в день",
            reward="Принять душ",
            time_to_complete=timedelta(minutes=1),
            publication_sign=True,
        )

    def test_habit_create(self):
        data = {
            "user": self.user.id,
            "place": "Дом",
            "time": "2024-06-22 22:26:00",
            "action": "Убраться по дому",
            "sign_pleasant_habit": False,
            "frequency": "Раз в день",
            "time_to_complete": timedelta(minutes=2),
            "reward ": "Посмотреть фильм",
            "publication_sign": True,
        }

        response = self.client.post(
            '/habits/create/',
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Habits.objects.all().exists()
        )

    def test_habit_list(self):
        response = self.client.get(
            '/habits/list'
        )

        print(response.json())

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {
                'count': 1,
                'next': None,
                'previous': None,
                'results': [
                    {'id': 4,
                     'place': 'Тренажерный зал',
                     'time': '2024-06-22 22:26:00',
                     'action': 'Занятие на беговой дорожке',
                     'sign_pleasant_habit': False,
                     'frequency': 'Раз в день',
                     'reward': 'Принять душ',
                     'time_to_complete': '00:01:00',
                     'publication_sign': True,
                     'user': 3,
                     'related_habit': None}
                ]
            }
        )

    def test_habit_retrieve(self):
        response = self.client.get(
            f'/habits/{self.habit.pk}/'
        )
        print(response.json())
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': 5,
             'place': 'Тренажерный зал',
             'time': '2024-06-22 22:26:00',
             'action': 'Занятие на беговой дорожке',
             'sign_pleasant_habit': False,
             'frequency': 'Раз в день',
             'reward': 'Принять душ',
             'time_to_complete': '00:01:00',
             'publication_sign': True,
             'user': 4,
             'related_habit': None}
        )

    def test_habit_update(self):
        new_data = {
            "reward": "Боль в мышцах",
            "time_to_complete": '00:01:30',
        }

        response = self.client.patch(
            f'/habits/update/{self.habit.pk}/',
            data=new_data
        )

        data = response.json()

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            data.get("reward"),
            "Боль в мышцах"
        )

    def test_habit_delete(self):
        response = self.client.delete(
            f'/habits/delete/{self.habit.pk}/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertEqual(
            Habits.objects.all().count(),
            0
        )
