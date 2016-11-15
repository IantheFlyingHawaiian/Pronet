from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render
from .models import Topic, Question
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
    output = {'topic_value': topic_value}

    #questions = get_object_or_404(Question, q_topic = topic_id)
    questions = Question.objects.all().filter(q_topic = topic_id)
    outputQuestions = {'questions' : questions}

    all_models_dict = {
        "topic_value": topic_value,
        "questions" : questions
    }



    return render(request, template_name,  all_models_dict)

# def questions(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)