from django.urls import path
from .views import PollsView, PollsWithAnswer

app_name = "polls"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('active_polls/', PollsView.as_view()),
    path(r'detailed_polls', PollsWithAnswer.as_view()),
    path('detailed_polls/', PollsWithAnswer.as_view())
]