from django.contrib import admin
from django.urls import path
from . import views
from . import apiviews
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rest_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

app_name = 'Polls'

# urlpatterns = [
#     path('polls/', views.polls_list, name="polls_list"),
#     path('polls/<int:pk>', views.polls_detail, name="polls_detail"),
# ]

router = DefaultRouter()
router.register('polls', apiviews.PollViewSet, base_name='polls')
schema_view = get_schema_view(
    openapi.Info(
        title="Polls API",
        default_version='v1',
        description='A simple API for django polls project',
        contact=openapi.Contact(email="adeyeyetimothy33@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

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
    path('list_users', apiviews.UserList.as_view(), name="user_list"),
    path('swagger-docs', schema_view.with_ui('swagger', cache_timeout=0)),
]

urlpatterns += router.urls

