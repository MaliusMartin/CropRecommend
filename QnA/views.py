from django.shortcuts import render
from .forms import QuestionForm
from .models import Question
from .utils import predict_answer
from .utils import preprocess_question
import numpy as np


def question_list(request):
    questions = Question.objects.all()
    return render(request, 'QnA/question_list.html', {'questions': questions})


def ask_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question_text = form.cleaned_data['question_text']
            # Preprocess the question
            preprocessed_question = preprocess_question(question_text)
            
            # Reshape the input data to a 2D array
            input_data_reshaped = np.array([preprocessed_question])
            
            # Call a function to predict the answer using the preprocessed question
            predicted_answer = predict_answer(input_data_reshaped)
            return render(request, 'QnA/answer.html', {'question_text': preprocessed_question, 'predicted_answer': predicted_answer})
    else:
        form = QuestionForm()
    return render(request, 'QnA/ask_question.html', {'form': form})

# def ask_question(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         if form.is_valid():
#             question_text = form.cleaned_data['question_text']
#             # Preprocess the question
#             preprocessed_question = preprocess_question(question_text)
            
#             # Reshape the input data to a 2D array
#             input_data_reshaped = np.array([preprocessed_question])
            
#             # Call a function to predict the answer using the preprocessed question
#             predicted_answer = predict_answer(input_data_reshaped)
#             return render(request, 'QnA/answer.html', {'question_text': preprocessed_question, 'predicted_answer': predicted_answer})
#     else:
#         form = QuestionForm()
#     return render(request, 'QnA/ask_question.html', {'form': form})


