from django.db import models

# Create your models here.

class Notification(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    sender = models.CharField(max_length=100)
    recipient = models.ForeignKey('Login.User', on_delete=models.CASCADE, related_name='received_notifications', default=None)

    def __str__(self):
        return self.title