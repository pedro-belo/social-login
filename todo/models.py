from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


# Create your models here.
class ToDo(models.Model):

    ADICIONADO = 1
    PROGRESSO = 2
    CONCLUIDO = 3

    STAGE_CHOICES = [
        (1, 'Adicionado'),
        (2, 'Progresso'),
        (3, 'Concluido')
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    task = models.CharField(max_length=50, blank=False)
    stage = models.PositiveSmallIntegerField(choices=STAGE_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
