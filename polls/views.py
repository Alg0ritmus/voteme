from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.http import HttpResponse

from .models import *

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')
	output = ', '.join([q.question_text for q in latest_question_list])
	context = {'latest_question_list':latest_question_list}		
	return render(request,'polls/index.html',context)

def detail(request, question_id):
	my_question = get_object_or_404(Question, pk = question_id)
	return HttpResponse("You're looking at question %s." % my_question.id)

def results(request, question_id):
	try:
		my_question = Question.objects.get(pk=question_id)
		context={"my_question":my_question}
		response = "You're looking at the results of question %s."
		return render(request,"polls/details.html",context)
	except Question.DoesNotExist:
		raise Http404("This page is not reachable!!!")

def create_vote(request,question_id):
	print('PKKK',question_id,"\n",request.POST)
	try:
		my_question = Question.objects.get(id=question_id)
		my_choice = my_question.choice_set.get(pk=request.POST['choice'])
		my_choice.votes+=1
		my_choice.save()
	except Exception as e:
			return HttpResponse("ERROR with create_vote",e)

	
	
	return redirect('/')


def create_poll(request):
	context={}
	return render(request,'polls/vote.html',context)

def post_poll(request):
	print('POSTKKK',"\n",request.POST,request.POST['choice1'])
	try:
		my_poll = Question(question_text=request.POST['question'], pub_date=timezone.now())
		my_poll.save()
		for a in range(1,len(request.POST)-1):
			choices = my_poll.choice_set.create(choice_text=request.POST['choice'+str(a)], votes=0)
		return redirect('/')
	except Exception as e:
		print(e)
		return HttpResponse("ERROR with create_vote",e)
