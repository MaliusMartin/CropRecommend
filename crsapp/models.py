from django.db import models

class CropRecommendation(models.Model):
  """
  Model to store user input for crop recommendation and the recommended crop.
  """
  # Soil Properties
  n = models.FloatField(verbose_name="Nitrogen Content (ppm)")
  p = models.FloatField(verbose_name="Phosphorus Content (ppm)")
  k = models.FloatField(verbose_name="Potassium Content (ppm)")

  # Climate Data
  temperature = models.FloatField(verbose_name="Average Annual Temperature (°C)")
  humidity = models.FloatField(verbose_name="Average Annual Humidity (%)")

  # Location (Optional)
  ph = models.FloatField(verbose_name="Soil pH", blank=True, null=True)
  rainfall = models.FloatField(verbose_name="Average Annual Rainfall (mm)", blank=True, null=True)

  # Recommended Crop
  recommended_crop = models.CharField(max_length=255, verbose_name="Recommended Crop")

  def __str__(self):
    return f"Crop Recommendation (ID: {self.id}) - Recommended Crop: {self.recommended_crop}"
