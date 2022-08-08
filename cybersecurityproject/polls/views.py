from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from . import forms
from django.utils import timezone

from .models import Choice, Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else: 
        selected_choice.votes+=1

        #Here the following code is vulnerable to SQL injection, the actual code is the fix i.e. using django models which sanitize data            
        #cursor = conn.cursor()
	    #command = """UPDATE Choice SET (vote) WHERE id=(id) VALUES (?,?) ;"""
        #data_tuple=(selected_choice.votes,id)
	    #cursor.execute(command,data_tuple)
	    #conn.commit()

        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def add_poll(request):
    if request.method == 'POST':
        form = forms.AddPoll(request.POST)
        formset = forms.QuestionMetaInlineFormset(request.POST)
        if form.is_valid() and formset.is_valid():
            
            #Here the following code is vulnerable to SQL injection, the actual code is the fix i.e. using django models which sanitize data            
            #cursor = conn.cursor()
	        #command = """INSERT INTO Question (question_text,pub_date) VALUES (?,?);"""
	        #data_tuple=(question_text,pub_date)
	        #cursor.execute(command,data_tuple)
	        #conn.commit()

            curForm = form.save(commit=False)
            curForm.save()
            pollMetas = formset.save(commit=False)
            for meta in pollMetas:
                meta.question = curForm
                meta.save()
            return redirect('polls:index')
    else:
        form = forms.AddPoll(initial={'pub_date': timezone.now()})
        product_meta_formset=forms.QuestionMetaInlineFormset()
    return render(request, 'polls/add_poll.html', {'form':form, 'product_meta_formset': product_meta_formset})
