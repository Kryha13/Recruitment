
from django.urls import path
from recruitment.views import MainPageView, AddMarkView, CandidatesListView


app_name = 'recruitment'

urlpatterns = [
    path('', MainPageView.as_view(), name='main'),
    path('add-mark/', AddMarkView.as_view(), name='add_mark'),
    path('candidates-list/', CandidatesListView.as_view(), name='candidates-list'),
]