from django.contrib import admin
from django.urls import path
from . import views
from . import apiviews
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rest_views

app_name = 'Polls'

# urlpatterns = [
#     path('polls/', views.polls_list, name="polls_list"),
#     path('polls/<int:pk>', views.polls_detail, name="polls_detail"),
# ]

router = DefaultRouter()
router.register('polls', apiviews.PollViewSet, base_name='polls')

urlpatterns = [
    # path('polls/', apiviews.PollList.as_view(), name="polls_list"),
    # path('polls/<int:pk>', apiviews.PollDetail.as_view(), name="polls_detail"),
    # path('choices/', apiviews.ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices', apiviews.ChoiceList.as_view(), name="choice_list"),
    # path('vote/', apiviews.CreateVote.as_view(), name="create_vote"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote', apiviews.CreateVote.as_view(), name="create_vote"),
    path('users', apiviews.UserCreate.as_view(), name="user_create"),
    path('login', apiviews.LoginView.as_view(), name="login"),
    # or
    # path('login', rest_views.obtain_auth_token, name="login"),
]

urlpatterns += router.urls
