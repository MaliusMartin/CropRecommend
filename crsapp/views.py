
from django.shortcuts import render
from .models import CropRecommendation  # Assuming model.py is in the same app
from joblib import load  # Assuming joblib is installed
from .forms import CropRecommendationForm
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the base directory of the current file
model_path = os.path.join(BASE_DIR, 'RecomendCropmodel.joblib')

def home(request):
    if request.method == 'POST':
        form = CropRecommendationForm(request.POST)
        if form.is_valid():
            # Get user input from the form (using model's field names)
            cleaned_data = form.cleaned_data

            # Prepare features as a list (aligned with model)
            features = [
                cleaned_data['n'],
                cleaned_data['p'],
                cleaned_data['k'],
                cleaned_data['temperature'],
                cleaned_data['humidity'],
                cleaned_data['ph'],
                cleaned_data['rainfall'],
            ]

            # Load the pre-trained model
            model = load(model_path)

            # Make prediction using the model
            prediction = model.predict([features])[0]

            # Get crop label based on prediction
            crop_label = get_crop_label(prediction)

            # Save user input and recommended crop to database (using model's field names)
            recommendation = CropRecommendation.objects.create(
                n=cleaned_data['n'],
                p=cleaned_data['p'],
                k=cleaned_data['k'],
                temperature=cleaned_data['temperature'],
                humidity=cleaned_data['humidity'],
                ph=cleaned_data['ph'],
                rainfall=cleaned_data['rainfall'],
                recommended_crop=crop_label,
            )

            # Render the result page with the recommended crop
            return render(request, 'crsapp/result.html', {'recommendation': recommendation, 'predicted_crop': crop_label})
    else:
        form = CropRecommendationForm()  # Create an empty form for initial display
    return render(request, 'crsapp/landingPage.html', {'form': form})

def get_crop_label(prediction):
    """
    This function maps the predicted label to the corresponding crop name.
    """
    crop_labels = {
        0: 'Soyabeans',
        1: 'Apple',
        2: 'Banana',
        3: 'Beans',
        4: 'Coffee',
        5: 'Cotton',
        6: 'Cowpeas',
        7: 'Grapes',
        8: 'Groundnuts',
        9: 'Maize',
        10: 'Mango',
        11: 'Orange',
        12: 'Peas',
        13: 'Rice',
        14: 'Watermelon',
    }
    return crop_labels.get(prediction)

def get_recommended_crop_data(request):
    # Your logic to retrieve the recommended crop data from the database (replace this)
    # This could involve querying the database based on the user's session or request data
    recommended_crop = None  # Placeholder for retrieved data
    return recommended_crop

def result(request):
    recommendation = get_recommended_crop_data(request)  # Call the data retrieval function
    return render(request, 'crsapp/result.html', {'recommendation': recommendation})
