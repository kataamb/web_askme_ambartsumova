from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger





TAGS = [
{
       "name" : i,
    } for i in ['bender', 'python', 'django', 'TechnoPark']
]

QUESTIONS = [
    {
        "id" : i,
        "title" : f"Question {i}",
        "text" : f"This is question number {i}",
        "tags": TAGS[:3],
    } for i in range(200)
]

ANSWERS = [
    {
        "id" : i,
        "title" : f"Answer {i}",
        "text" : f"This is answer number {i}",
    } for i in range(200)
]


def paginate(objects_list, request, per_page=10):
    page_num = request.GET.get('page', 1)
    paginator = Paginator(objects_list, per_page)

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(1)
    except Exception:
        page_obj = paginator.page(1)


    return page_obj


def index(request):
    questions = paginate(QUESTIONS, request)
    return render(request, template_name="index.html", context={"questions" : questions})

def hot(request):
    questions = paginate(QUESTIONS[5:50:2], request, 5)
    return render(request, template_name="hot.html", context={"questions" : questions})

def login(request):
    return render(request, template_name="login.html")

def register(request):
    return render(request, template_name="signup.html")

def ask(request):
    return render(request, template_name="ask.html")

def settings(request):
    return render(request, template_name="settings.html")


def question(request, question_id):
    question = QUESTIONS[question_id]
    answers = paginate(ANSWERS[:10], request, 2)
    return render(request, template_name="question.html", context={"question": question, "answers": answers})

def tag(request, tag_slug):
    questions = paginate(QUESTIONS[::5], request)
    return render(request, template_name="tag.html", context={"tag_name": tag_slug, "questions": questions})

