from django.shortcuts import render

# Create your views here.
from web.forms import QuestionsForm
from web.forms import AnswersForm
from web.models import Student
from web.models import Question



def index(request):
    students = Student.objects.all()
    questions = Question.objects.all()
    answersform = AnswersForm()
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AnswersForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            cleaned_data = request.POST.getlist('answer')
            print(cleaned_data)


    return render(request, 'index.html', {'students': students, 'answersform': answersform, 'questions':questions})