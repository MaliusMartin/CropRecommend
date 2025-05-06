from django.shortcuts import render
from joblib import load
from .forms import InputForm

# Load the Random Forest Regressor model and encoders
def load_random_forest_model():
    model_path = 'models/RandomForest_regressor_model.joblib'
    return load(model_path)

# Optional: Load encoders used during training (for area and item if they're categorical)
area_encoder = load('models/area_encoder.joblib')
item_encoder = load('models/item_encoder.joblib')

# Load the model once when the module loads
rf_model = load_random_forest_model()

def index(request):
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            area = form.cleaned_data['area']
            item = form.cleaned_data['item']
            year = form.cleaned_data['year']
            rainfall = form.cleaned_data['average_rain_fall_mm_per_year']
            pesticides = form.cleaned_data['pesticides_tonnes']
            temp = form.cleaned_data['avg_temp']

            # Encode categorical variables
            encoded_area = area_encoder.transform([area])[0]
            encoded_item = item_encoder.transform([item])[0]

            # Prepare input features
            feature_array = [[encoded_area, encoded_item, year, rainfall, pesticides, temp]]

            # Predict yield
            predicted_yield = rf_model.predict(feature_array)[0]

            return render(request, 'Yieldapp/results.html', {'predicted_yield': predicted_yield})

    else:
        form = InputForm()

    return render(request, 'Yieldapp/index.html', {'form': form})



# from django.shortcuts import render
# from django.http import JsonResponse
# from joblib import load
# from .forms import InputForm


# # Load the Bagging Regressor model
# def load_bagging_regressor_model():
#     model_path = 'models/Random Forest_model.joblib' 
#     return load(model_path)

# bagging_model = load_bagging_regressor_model()

# def index(request):
#     if request.method == 'POST':
#         form = InputForm(request.POST)
#         if form.is_valid():
#             area = form.cleaned_data['area']
#             item = form.cleaned_data['item']
#             year = form.cleaned_data['year']
#             rainfall = form.cleaned_data['average_rain_fall_mm_per_year']
#             pesticides = form.cleaned_data['pesticides_tonnes']
#             temp = form.cleaned_data['avg_temp']

#             # Prepare input features for prediction
#             feature_array = [[area, item, year, rainfall, pesticides, temp]]

#             # Make prediction using the loaded Bagging Regressor model
#             predicted_yield = bagging_model.predict(feature_array)[0]

#             # Render results.html with predicted yield
#             return render(request, 'Yieldapp/results.html', {'predicted_yield': predicted_yield})

#     else:
#         form = InputForm()

#     return render(request, 'Yieldapp/index.html', {'form': form})
















