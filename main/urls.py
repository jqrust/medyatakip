from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('',views.home_view,name="home"),
    path('login/',views.LoginView.as_view(),name="login"),
    path('logout/',views.logout_view,name="logout"),    

    path('survey/',views.SurveyList.as_view(),name="survey_list"),
    path('survey/create/',views.SurveyCreate.as_view(),name="survey_create"),
    path('survey/<int:pk>/',views.SurveyDetail.as_view(),name="survey_detail"),
    path('survey/<int:pk>/delete/',views.SurveyDelete.as_view(),name="survey_delete"),
    path('survey/<int:pk>/update/',views.SurveyUpdate.as_view(),name="survey_update"),
    path('survey/<int:pk>/question_create/',views.QuestionCreate.as_view(),name="question_create"),
    path('survey/<int:pk>/<int:pk_q>/',views.QuestionDetail.as_view(),name="question_detail"),
    path('survey/<int:pk>/<int:pk_q>/delete/',views.QuestionDelete.as_view(),name="question_delete"),
    path('survey/<int:pk>/<int:pk_q>/answer_create/',views.AnswerCreate.as_view(),name="answer_create"),
    path('survey/<int:pk>/<int:pk_q>/<int:pk_answer>/',views.AnswerUpdate.as_view(),name="answer_update"),
    path('survey/<int:pk>/<int:pk_q>/<int:pk_answer>/delete',views.AnswerDelete.as_view(),name="answer_delete"),

    path('publication/',views.PublicationList.as_view(),name="publication_list"),
    path('publication/<int:pk>',views.PublicationDetail.as_view(),name="publication_detail"),
]