from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views

app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.create_question, name='create_question'),
    path('question/modify/<int:question_id>/', question_views.edit_question,
         name='edit_question'),
    path('question/delete/<int:question_id>/', question_views.delete_question,
         name='delete_question'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.edit_answer, name='edit_answer'),
    path('answer/delete/<int:answer_id>/', answer_views.delete_answer, name='delete_answer'),

    # comment_views.py
    path('comment/create/question/<int:question_id>/', comment_views.comment_create_question,
         name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_edit_question,
         name='comment_edit_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question,
         name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer,
         name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_edit_answer,
         name='comment_edit_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer,
         name='comment_delete_answer'),

    # vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]