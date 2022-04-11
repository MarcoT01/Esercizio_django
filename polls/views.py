from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, request
from django.middleware.csrf import get_token
from django.shortcuts import render
from django.urls import reverse_lazy, reverse

from .models import Question, Choice
from django.views import generic


def home(request):
    return render(request, "polls/polls_home.html")

    def get_success_url(self):
        return reverse_lazy('polls:question_detail')


class QuestionListView(LoginRequiredMixin, generic.ListView):
    model = Question
    template_name = "polls/question_list.html"


class QuestiondetailView(generic.DetailView):
    model = Question
    template_name = "polls/question_detail.html"


class QuestionCreateView(generic.CreateView):
    model = Question
    fields = ["q_text", "pub_date"]
    template_name = "polls/question_create.html"
    success_url = reverse_lazy("polls:question_list")


class QuestionUpdateView(generic.UpdateView):
    model = Question
    fields = ["q_text", "pub_date"]
    template_name = "polls/question_update.html"
    success_url = reverse_lazy("polls:question_list")


class QuestiondeleteView(generic.DeleteView):
    model = Question
    template_name = "polls/question_delete.html"
    success_url = reverse_lazy("polls:question_list")


# def login_required(function):
#     if user.is_authenticated:
#         return function
#     else:

@login_required
def vote(request):
    if request.method != "POST":
        return HttpResponseRedirect(reverse('polls_question_list'))
    choice_id = int(request.POST["choice"])
    c = Choice.objects.get(id=choice_id)
    c.votes += 1
    c.save()
    return HttpResponseRedirect(reverse("polls:question_detail", kwargs={"pk": c.question.id}))
