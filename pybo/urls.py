from django.urls import path
from .views import base_views, question_views, answer_views, comment_views, vote_views

# 네임스페이스 : pybo앱 이외 다른 앱이 이 프로그램에 추가될 수 있다.
#              이 때 서로 다른 앱끼리 같은 URL 별칭을 사용하면 중복 문제가 생긴다.
#              이 문제를 해결하기 위한 개념
#              즉, 각각의 앱이 관리하는 독립된 이름 공간이다.
app_name = 'pybo'

# URL 별칭 사용
# /pybo/   -> index  라는   URL 별칭을
# /pybo/2/ -> detail 이라는 URL 별칭을
urlpatterns = [
    # base_views.py
    path('', base_views.index, name='index'),
    path('<int:question_id>/', base_views.detail, name='detail'),

    # question_views.py
    path('question/create/', question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>', question_views.question_modify,
        name='question_modify'),
    path('question/delete/<int:question_id>/', question_views.question_delete,
        name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>', answer_views.answer_modify,
        name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete,
        name='answer_delete'),

    # comment_views.py
    path('comment/create/question/<int:question_id>/', 
        comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', 
        comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', 
        comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/', 
        comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', 
        comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', 
        comment_views.comment_delete_answer, name='comment_delete_answer'),

    # vote_views.py
    path('vote/question/<int:question_id>',
        vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>',
        vote_views.vote_answer, name='vote_answer'),
]