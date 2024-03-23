
## Crop Recommendation System

This repository contains a machine learning-based crop recommendation system built using Python and Django. The system leverages a Random Forest classifier to suggest suitable crops based on environmental factors such as temperature, humidity, rainfall, and soil type.

### Recommended Crops:
The model is capable of recommending the following crops:
- Rice
- Maize
- Soybeans
- Beans
- Peas
- Groundnuts
- Cowpeas
- Banana
- Mango
- Grapes
- Watermelon
- Apple
- Orange
- Cotton
- Coffee

These crops cover a diverse range of agricultural produce, enabling farmers to make informed decisions based on their specific agricultural conditions.


## Features:
User Interface: Provides a user-friendly interface for farmers to input environmental parameters.
Crop Prediction: Utilizes a trained RandomForestClassifier model to predict suitable crops based on the input parameters.
Data Visualization: Visualizes crop recommendations and related information for better understanding.
Admin Dashboard: Includes an admin dashboard to manage users, crops, and other system components.
Technologies Used:
Django: Web framework for backend development.
HTML/CSS/JavaScript: Frontend development for user interface.
Pandas: Data manipulation and preprocessing.
Scikit-learn: Machine learning library for training and deploying the crop recommendation model.
Joblib: Used for model persistence.
Bootstrap: Frontend framework for responsive design.
SQLite/PostgreSQL: Database management system for storing user data and crop information.
GitHub: Version control and project management.

### Usage:
To use this system locally, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment:
    ```bash
    python3 -m venv env
    ```
4. Activate the virtual environment:
    - On Windows:
    ```bash
    env\Scripts\activate
    ```
    - On macOS and Linux:
    ```bash
    source env/bin/activate
    ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the Django server:
    ```bash
    python manage.py runserver
    ```
7. Access the application in your web browser at `http://localhost:8000`.

## Future Enhancements:
Implement more sophisticated machine learning algorithms for crop prediction.
Enhance user interface and data visualization capabilities.
Integrate external APIs for weather forecasting and agricultural data.
Provide personalized recommendations based on historical data and user preferences.
Explore additional factors (e.g., market prices) for comprehensive recommendations.

### Feedback and Contributions:
Feedback, bug reports, and contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

---

## License:
This project is licensed under the `MIT License`.

Author:
`MaliusMartin`