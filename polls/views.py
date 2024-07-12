from django.http import HttpResponse
from django.views.generic import (ListView, DetailView)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Question, Choice
from django.urls import reverse_lazy


def index(request):
    return HttpResponse("Hello world. You're at the polls index.")


class QuestionListView(ListView):
    model = Question
    queryset = Question.objects.all().order_by("-pub_date")

class QuestionDetailView(DetailView):
    model = Question

class QuestionCreateView(UpdateView):
    model = Question
    fields = ["question_text", "pub_date"]
    success_url = reverse_lazy("question-list")

class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["question_text", "pub_date"]

    def get_success_url(self) -> str:
        return reverse_lazy(
            "question-detail",
            kwargs={"pk": self.object.id}
        )

class QuestionDeleteView(DeleteView):
    model = Question
    success_url = reverse_lazy("question-list")


class ChoiceListView(ListView):
    model = Choice
    queryset = Choice.objects.all()

class ChoiceDetailView(DetailView):
    model = Choice

class ChoiceCreateView(CreateView):
    model = Choice
    fields = ["question", "choice_text", "votes"]
    success_url = reverse_lazy("choice-list")

class ChoiceUpdateView(UpdateView):
    model = Choice
    fields = ["choice_text", "votes"]

    def get_success_url(self) -> str:
        return reverse_lazy(
            "choice-detail",
            kwargs={"pk": self.object.id}
        )

class ChoiceDeleteView(DeleteView):
    model = Choice
    success_url = reverse_lazy("choice-list")