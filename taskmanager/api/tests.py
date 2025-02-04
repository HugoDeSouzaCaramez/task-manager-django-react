from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task

class TaskTests(APITestCase):
    def setUp(self):
        self.task = Task.objects.create(
            title='Tarefa Inicial',
            description='Descrição da tarefa inicial',
            is_completed=False
        )

    def test_list_tasks(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_task(self):
        url = reverse('task-list')
        data = {
            'title': 'Nova Tarefa',
            'description': 'Descrição da nova tarefa',
            'is_completed': True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_create_task_without_title(self):
        url = reverse('task-list')
        data = {
            'description': 'Tarefa sem título',
            'is_completed': False
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)