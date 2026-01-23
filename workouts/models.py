from django.db import models

# Create your models here.
class Exercise(models.Model):
    """Названия упражнений"""
    name = models.CharField(
        max_length=20,
        unique=True,
        verbose_name='Название упражнения'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'
        ordering = ['name']
    def __str__(self):
        return self.name