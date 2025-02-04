from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Task(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)  # Adicionado relacionamento com User
    title = models.CharField(max_length=200)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)