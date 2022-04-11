from django.db import models


class Question(models.Model):
    q_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f"{self.pub_date.strftime('%Y-%m-%d-%M-%S')} - {self.q_text}"


class Choice(models.Model):
    choice_text = models.CharField(max_length=100)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices")
    votes = models.IntegerField(default=0)

#   class Meta:
#       verbose_name_plural = "Scelta"
