from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    content=models.CharField(max_length=1024)
    slug=models.SlugField()
    def __str__(self):
        return self.content


class Answer(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)
    choice=models.ForeignKey('Choice',on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{}-{}".format(self.choice,self.user)

class Choice(models.Model):
    question=models.ForeignKey('Question',on_delete=models.CASCADE)
    content=models.CharField(max_length=256)

    @property
    def answer_count(self):
        count=Answer.objects.filter(
            question=self.question,
            choice=self.id
        ).count()
        return count


    def __str__(self):
        return "{}-{}".format(self.question.content[:50]  ,  self.content)



