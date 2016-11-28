from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_text = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_text


class Question(models.Model):
    q_topic_id = models.ForeignKey(Topic, on_delete=models.PROTECT, default = None)
    question_text = models.CharField(max_length=200, default = "")
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=200, default = "")
    #answers = models.ManyToManyField(Answer)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    a_question_topic_id = models.ForeignKey(Question, on_delete=models.PROTECT, default = None)
    answer_text = models.CharField(max_length=200)
    author = models.CharField(max_length =200, default = "")
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.answer_text

'''
class Post(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    post_text = models.CharField(max_length = 500)

    def __str__(self):
        return self.post_text
'''