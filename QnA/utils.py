from spellchecker import SpellChecker
from joblib import load
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the base directory of the current file
MODEL_PATH = os.path.join(BASE_DIR, 'AgriQ&A_model.joblib.gz')

def preprocess_question(question):
    # Spell checking
    spell = SpellChecker()
    words = question.split()
    corrected_words = [spell.correction(word) for word in words]
    corrected_question = ' '.join(corrected_words)
    
    return corrected_question

def predict_answer(question):
    
    model = load(MODEL_PATH)
        # Call any preprocessing necessary (like TF-IDF vectorization)
        
        # Make predictions
    predicted_answer = model.predict([question])
    return predicted_answer
    
# def predict_answer(question):
#     try:
#         # Load the trained model
#         model = load(MODEL_PATH)
#         # Call any preprocessing necessary (like TF-IDF vectorization)
        
#         # Make predictions
#         predicted_answer = model.predict([question])
#         return predicted_answer
#     except Exception as e:
#         print(f"An error occurred while predicting answer: {e}")
#         return None