from django.db import models


class Property(models.Model):
    """
    Объект интеллектуальной собственности
    """
    author = models.CharField(max_length=255)
    hash_sum = models.CharField(max_length=64, unique=True)
    timestamp = models.PositiveIntegerField()
