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
            user_answers = request.POST.getlist('answer')
            user_questions = request.POST.getlist('question')

            questions_with_answers = []
            for (pk, ans) in zip(user_questions, user_answers):
                question = Question.objects.filter(pk=pk).first()
                questions_with_answers.append((question, ans))
            print(questions_with_answers)

            # questions_with_answers = zip(user_questions, user_answers)
            return render(request, 'show_answers.html',
                          {'students': students, 'answersform': answersform, 'questions': questions_with_answers})

    return render(request, 'index.html', {'students': students, 'answersform': answersform, 'questions': questions})

