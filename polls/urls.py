from django.urls import path
from . import views as v

app_name = 'polls'

urlpatterns = [
    path('', v.IndexView.as_view(), name='index'),
    path('<int:pk>', v.DetailView.as_view(), name='detail'),
    path('<int:pk>/results', v.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote', v.vote, name='vote'),
]
