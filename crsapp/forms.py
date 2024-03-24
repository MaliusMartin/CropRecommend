from django import forms
from .models import CropRecommendation

class CropRecommendationForm(forms.ModelForm):
  class Meta:
    model = CropRecommendation
    fields = ['n', 'p', 'k', 'temperature', 'humidity', 'ph', 'rainfall']
    labels = {
      'n': 'Nitrogen Content (ppm)',
      'p': 'Phosphorus Content (ppm)',
      'k': 'Potassium Content (ppm)',
      'temperature': 'Average Annual Temperature (°C)',
      'humidity': 'Average Annual Humidity (%)',
      'ph': 'Soil pH',
      'rainfall': 'Average Annual Rainfall (mm)',
    }

  def __init__(self, *args, **kwargs):
    super(CropRecommendationForm, self).__init__(*args, **kwargs)
    for field in self.fields:
      self.fields[field].widget.attrs.update({'class': 'form-control'})


