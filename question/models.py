from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
	content = models.CharField(max_length = 100)
	score = models.CharField(max_length = 2)
	answer = models.CharField(max_length = 10)
	time = models.DateField(auto_now = True)

class Answerecord(models.Model):
	user_id = models.ForeignKey(User)
	question_id = models.ForeignKey(Questions)
	start_time = models.DateField()
	end_time = models.DateField()
	total_time = models.DateField()
	answer = models.CharField(max_length = 10)

class Editrecord(models.Model):
	question_id = models.ForeignKey(Questions)
	user_id = models.ForeignKey(User)
	num = models.CharField(max_length = 2)
	answer = models.CharField(max_length = 10)
