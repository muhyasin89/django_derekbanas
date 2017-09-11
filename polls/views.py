# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

from .models import Question, Choice

from django.shortcuts import get_object_or_404

from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context={
        'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)
    #output = ', '.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)

def test_page(request):
    return HttpResponse("this is test page")

def detail(request, question_id):
    question =get_object_or_404(Question, pk=question_id)

    #return HttpResponse("Your looking at question %s" % question_id)
    return render(request, 'polls/detail.html',{'question': question})

def results(request, question_id = None):
    #response = "You're looking at the results of question %s"
    #return HttpResponse(response % question_id)
    question =  get_object_or_404(Question, pk=question_id)

    return render(request, 'polls/result.html', {'question': question})


def vote(request, question_id):
    #return HttpResponse("You're voting on question %s" % question_id)
    question = get_object_or_404(Question, pk =question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_message': "You didin't select  a choice"
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:result'), args=(question.id,))
