from django.db import models

class Task(models.Model):
    title = models.CharField('Name', max_length=50)
    task = models.TextField('Content')

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

        
class Work(models.Model):

    ISHAPPY_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('neutral', 'Neutral')
    ]

    name = models.CharField('Name', max_length=50)
    selery = models.IntegerField()
    isHappy = models.CharField(
        max_length=10,
        choices = ISHAPPY_CHOICES,
        default= 'neutral'
    )

    def __str__(self):
        return self.name 

    class Meta:
        verbose_name = 'work'
        verbose_name_plural = 'works'