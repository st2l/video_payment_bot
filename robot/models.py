from django.db import models
from django.contrib.auth import get_user_model


class TelegramUser(models.Model):
    user = models.OneToOneField(
        to=get_user_model(),
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='telegram_user'
    )
    chat_id = models.CharField(
        max_length=20
    )
    balance = models.IntegerField(
        default=0
    )

    def __str__(self) -> str:
        return self.chat_id

    def get_user(self):
        return self.user

    def set_user(self, user):
        self.user = user
        self.save()

class Video(models.Model):
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='videos/')
    
    def __str__(self) -> str:
        return self.title
    
