from django.contrib.auth.models import User
from django.db import models

# 질문 모델 (글쓴이, 제목, 내용, 작성일시, 수정일시, 추천)
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    # 데이터 조회 시 id가 아닌 제목을 표시
    def __str__(self):
        return self.subject

# 답변 모델 (글쓴이, 질문, 내용, 작성일시, 수정일시)
class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

# on_delete=models.CASCADE : 계정이 삭제되면 계정과 연결된 Question 모델 데이터 모두 삭제

# 댓글 모델 (댓쓴이, 댓글 내용, 작성일시, 수정일시, 댓글이 달린 질문, 댓글이 달린 답변)
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, 
                                on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)