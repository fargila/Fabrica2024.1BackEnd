from django.db import models

class Atividade(models.Model):
    activity = models.CharField(verbose_name="activity", max_length=150, blank=True, null=True)
    type = models.CharField(verbose_name="type", max_length=20, blank=True, null=True)
    participants = models.IntegerField(verbose_name="participants", blank=True, null=True)
    price = models.FloatField(verbose_name="price", blank=True, null=True)
    link = models.CharField(verbose_name="link", max_length=50, blank=True, null=True)
    key = models.CharField(verbose_name="key", max_length=15, blank=True, null=True)
    acessibility = models.FloatField(verbose_name="acessibility", blank=True, null=True)
    
    def __str__(self) -> str:
        return f'{self.activityc}'
