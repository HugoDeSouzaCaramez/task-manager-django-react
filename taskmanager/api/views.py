from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = [permissions.IsAuthenticated]  # Autenticação JWT
    permission_classes = []

    #def perform_create(self, serializer):
        #serializer.save(user=self.request.user)  # Associa a tarefa ao usuário logado