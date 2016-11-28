from django.http import HttpResponse
from django.views import generic
import logging
from django.template import loader
from django.shortcuts import render, redirect
from .models import Topic, Question, Answer
from .forms import QuestionForm, AnswerForm
from django.shortcuts import get_object_or_404
import datetime
from django.utils import timezone

def forums(request):
     template_name = "forums/forumList.html"
     return render(request, template_name)

#lists all topics instead of pictures
def index(request):
    template_name = "forums/index.html"
    topic = Topic.objects.all()
    latest_topic_list = topic.order_by('topic_text')[:5]
    output = {'latest_topic_list': latest_topic_list}
    return render(request, template_name, output)


def topic(request, topic_text):
    template_name = "forums/Topic.html"
    try:
        topic_value = get_object_or_404(Topic, topic_text= topic_text)
    except Topic.DoesNotExist:
        raise Http404("Topic does not exist")
    temp_id = topic_value.id
    questions = Question.objects.all().filter(q_topic_id = temp_id)
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
    answers = Answer.objects.all().filter(a_question_topic_id = question_id)
    all_models_dict = {
        "question_value": question_value,
        "answers": answers,
    }
    return render(request, template_name, all_models_dict)

#used for forms
def question_new(request, topic_id):
    template_name = "forums/question_edit.html"
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.q_topic_id = Topic.objects.get(topic_text = topic_id)
            question.pub_date = timezone.now()
            question.author = request.user
            author_name = question.author.name
            question.author = author_name
            question.save()

            # This text takes you to culinary id = 1
            #text = "/forums/" +  str(question.q_topic_id.id)

            #this text takes you forums/culinary
            #text = "/forums/" + str(question.q_topic_id)

            # this text takes you forums/culinary/question_id
            text = "/forums/" + str(question.q_topic_id) + "/" + str(question.pk)

            return redirect(text)
    else:
        form = QuestionForm()
    return render(request, template_name, {'form': form})

def add_answer_to_question(request, question_id, topic_id):
    template_name = "forums/AATQ.html"

    #question = get_object_or_404(Question, pk = question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.a_question_topic_id = Question.objects.get(question_text=question_id)
            answer.author = request.user
            author_name = answer.author.name
            answer.author = author_name
            answer.pub_date = timezone.now()
            answer.save()
            text = "/forums/" + str(topic_id) + "/" + str(answer.a_question_topic_id.id)
            return redirect(text)
    else:
        form = AnswerForm()
    return render(request, template_name, {'form':form})

