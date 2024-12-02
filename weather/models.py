from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    data = models.JSONField()  # Store the API response
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city
