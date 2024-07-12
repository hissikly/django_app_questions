from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "question/",
        views.QuestionListView.as_view(),
        name="question-list"
    ),
    path(
        "question/<int:pk>",
        views.QuestionDetailView.as_view(),
        name="question-detail"
    ),
    path(
        "question/create",
        views.QuestionCreateView.as_view(),
        name="question-create"
    ),
    path(
        "question/<int:pk>/update",
        views.QuestionUpdateView.as_view(),
    ),

    path(
        "choice/",
        views.ChoiceListView.as_view(),
        name="choice-list"
    ),
    path(
        "choice/<int:pk>",
        views.ChoiceDetailView.as_view(),
        name="choice-detail"
    ),
    path(
        "choice/create",
        views.ChoiceCreateView.as_view(),
        name="choice-create"
    ),
    path(
        "choice/<int:pk>/update",
        views.ChoiceUpdateView.as_view(),
    ),
]