from django.db import models

class Question(models.Model):
	question_text = models.CharField(max_length=255, null=False)
	closed = models.BooleanField()
	pub_date = models.DateField()

	def __str__(self):
		return self.question_text

	def changeStatus(self):
		self.closed = not self.closed
		self.save()

	
	def withdrawChoice(self, choice_id):
		c = Choice.objects.get(id = choice_id)
		c.votes = 0
		c.save()
		self.choices.remove(c)


class Choice(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices", null=True)
	choice_text = models.CharField(max_length=50)
	votes = models.IntegerField()

	def __str__(self):
		return self.choice_text

	@property
	def percent(self):
		
		amount = 0
		
		for vote in self.question.choices.all():
			amount = amount + vote.votes
		
		percents = float(self.votes * 100) / amount
		#return ("%.2f" % (percents)) 
		return round(percents, 2) 

	def addvote(self):
		self.votes = self.votes + 1
		self.save()

	def addchoice(self, question):
		self.question = question
		self.save()