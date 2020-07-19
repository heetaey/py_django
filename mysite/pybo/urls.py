from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.create_question, name='create_question'),
    path('question/modify/<int:question_id>/', views.edit_question, name='edit_question'),
    path('question/delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('answer/modify/<int:answer_id>/', views.edit_answer, name='edit_answer'),
    path('answer/delete/<int:answer_id>/', views.delete_answer, name='delete_answer'),
    path('comment/create/question/<int:question_id>/', views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_edit_question,
         name='comment_edit_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question,
         name='comment_delete_question'),
]