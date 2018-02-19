from django.shortcuts import render

# Create your views here.
from web.forms import QuestionsForm
from web.forms import AnswersForm
from web.models import Student
from web.models import Question



def index(request):
    students = Student.objects.all()
    questions = Question.objects.all()
    questionsform = QuestionsForm()
    answers = AnswersForm()

    return render(request, 'index.html', {'students': students, 'questionsform': questionsform, 'answers': answers, 'questions':questions})