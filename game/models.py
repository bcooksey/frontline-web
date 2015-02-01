from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)
    lasted_updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Game {}'.format(self.id)
