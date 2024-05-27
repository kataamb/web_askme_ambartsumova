from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger

from app.models import*

from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login, authenticate

from app.forms import*




TAGS = [
{
       "name" : i,
    } for i in ['bender', 'python', 'django', 'TechnoPark']
]
'''
QUESTIONS = [
    {
        "id" : i,
        "title" : f"Question {i}",
        "text" : f"This is question number {i}",
        "tags": TAGS[:3],
    } for i in range(200)
]
'''

'''
ANSWERS = [
    {
        "id" : i,
        "title" : f"Answer {i}",
        "text" : f"This is answer number {i}",
        "likes_count":1
    } for i in range(200)
]
'''

def paginate(objects_list, request, per_page=10):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)

    try:
        page_obj = paginator.page(page_num)
    except (PageNotAnInteger, EmptyPage, Exception):
        page_obj = paginator.page(1)


    return page_obj

@login_required()
def index(request):
    QUESTIONS = Question.objects.new_questions()

    questions = paginate(QUESTIONS, request)
    return render(request, template_name="index.html", context={"questions" : questions})

def hot(request):
    QUESTIONS = Question.objects.hot_questions()
    questions = paginate(QUESTIONS, request, 5)
    return render(request, template_name="hot.html", context={"questions" : questions})

@require_http_methods(['GET', 'POST'])
def log_in(request):
    if request.method == 'GET':
        login_form = LoginForm()
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            print(login_form.cleaned_data)

            user = authenticate(request, **login_form.cleaned_data)

            if user:
                login(request, user)
                return redirect(reverse('index'))
        print('Failed to login')
    #return render(request, "login.html", context={"form": login_form})
    return render(request, template_name="login.html", context={"form" : login_form})

def register(request):
    return render(request, template_name="signup.html")

def ask(request):
    return render(request, template_name="ask.html")

def settings(request):
    return render(request, template_name="settings.html")


def question(request, question_id):
    question = Question.objects.get_by_pk(question_id)
    ANSWERS = Answer.objects.get_by_question(question_id)
    answers = paginate(ANSWERS, request, 2)
    return render(request, template_name="question.html", context={"question": question, "answers": answers})

def tag(request, tag_slug):
    QUESTIONS = Question.objects.get_by_tag(tag_slug)
    questions = paginate(QUESTIONS, request)
    return render(request, template_name="tag.html", context={"tag_name": tag_slug, "questions": questions})

