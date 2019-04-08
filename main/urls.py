from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('',views.home_view,name="home"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('survey/create/',views.SurveyCreate.as_view(),name="survey_create"),
]