from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render
from .models import Topic, Question, Answer
from django.shortcuts import get_object_or_404

def forums(request):
     template_name = "forums/forumList.html"
     return render(request, template_name)

#hi there
def index(request):
    template_name = "forums/index.html"
    topic = Topic.objects.all()
    latest_topic_list = topic.order_by('topic_text')[:5]
    output = {'latest_topic_list': latest_topic_list}
    return render(request, template_name, output)


def topic(request, topic_id):
    template_name = "forums/Topic.html"
    try:
        topic_value = get_object_or_404(Topic, pk=topic_id)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist")
    #output = {'topic_value': topic_value}
    #questions = get_object_or_404(Question, q_topic = topic_id)
    questions = Question.objects.all().filter(q_topic_id = topic_id)
    #answers = Answers.objects.all().filter(a_question_topic_id = question_id)
    all_models_dict = {
        "topic_value": topic_value,
        "questions" : questions
    }
    return render(request, template_name,  all_models_dict)


def questions(request, question_id, topic_id):
    template_name = "forums/QA.html"
    try:
        question_value = get_object_or_404(Question, pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #outputA = {'question_value': question_value}
    answers = Answer.objects.all().filter(a_question_topic_id = question_id)

    all_models_dict = {
        "question_value": question_value,
        "answers": answers
    }
    return render(request, template_name, all_models_dict)
