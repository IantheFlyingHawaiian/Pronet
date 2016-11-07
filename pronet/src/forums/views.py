from django.http import HttpResponse
from django.views import generic
from django.template import loader
from django.shortcuts import render

def forums(request):
    template_name = "forums/forumList.html"
    return render(request, template_name)

#hi there
def topics(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def questions(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)