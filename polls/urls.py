from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path('home/', views.home, name="home_page"),
    path('questions/', views.QuestionListView.as_view(), name="question_list"),
    path('questions/<int:pk>/', views.QuestiondetailView.as_view(), name="question_detail"),
    path('questions/create/', views.QuestionCreateView.as_view(), name="question_create"),
    path('questions/<int:pk>/edit/', views.QuestionUpdateView.as_view(), name="question_update"),
    path('questions/<int:pk>/delete/', views.QuestiondeleteView.as_view(), name="question_delete"),
    path('vote/', views.vote, name="vote")
]
