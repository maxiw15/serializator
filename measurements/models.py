from django.db import models


class Sensor(models.Model):
    """Датчик"""
    name = models.CharField(max_length=30)
    value = models.CharField(max_length=100)


class Measurement(models.Model):
    """Измерение температуры"""
    value = models.FloatField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

