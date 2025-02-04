from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from api.models import Task  

User = get_user_model()

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados iniciais'

    def handle(self, *args, **kwargs):
        self.stdout.write("Criando usuários e tarefas...")

        # Criar superusuário
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Superusuário criado!'))

        # Criar usuário comum
        common_user = User.objects.create_user(
            username='usuario1',
            password='senha123',
            email='usuario1@example.com'
        )

        # Criar tarefas
        tasks = [
            {
                'title': 'Django',
                'description': 'seeds',
                'is_completed': False
            },
            {
                'title': 'Fazer compras',
                'description': 'Comprar itens essenciais',
                'is_completed': True
            }
        ]

        for task_data in tasks:
            Task.objects.create(**task_data)

        self.stdout.write(self.style.SUCCESS('Dados iniciais criados com sucesso!'))