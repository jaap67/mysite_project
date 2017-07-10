from django.shortcuts import render, redirect
from pools.models import Question, Choice

def index(request):
	return render(request, 'index.html', { "questions" : Question.objects.all().order_by('-pub_date') })

def questions(request, question_id):
	#print ('id recebido: %s' % (question_id))
	question = Question.objects.get(id = question_id)
	return render(request, 'question.html', { "question" : question })

def results(request, question_id):
	result = Question.objects.get(id = question_id)
	return render(request, 'question.html', { "result" : result })

def vote(request, question_id):
	vote = Question.objects.get(id = question_id)
	return render(request, 'votes.html', { "vote" : vote })

def addvote(request, choice_id):
	choice = Choice.objects.get(id = choice_id)
	choice.addvote()
	return redirect('index')

def manage(request, question_id):
	question = Question.objects.get(id = question_id)
	return render(request, 'manage.html', { "question" : question, "choices" : Choice.objects.all() })

def withdrawChoice(request, question_id, choice_id):
	question = Question.objects.get(id = question_id)
	question.withdrawChoice(choice_id)
	return redirect('manage', question_id)

def changeStatus(request, question_id):
	question = Question.objects.get(id = question_id)
	question.changeStatus()
	return redirect('manage', question_id)

def addchoice(request, question_id, choice_id):
	question = Question.objects.get(id = question_id)
	c = Choice.objects.get(id = choice_id)
	c.addchoice(question)
	return redirect('manage', question_id)