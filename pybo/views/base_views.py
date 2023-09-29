from django.core.paginator import Paginator # 장고의 페이징 처리 클래스 사용
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Question

def index(request):

    """
    pybo 목록 출력
    """

    # 입력 인자
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    so = request.GET.get('so', 'recent') # 정렬 기준
    # 기본값을 1로 설정
    # GET 방식 요청 URL 예 : localhost:8000/pybo/?page=1

    # 정렬
    if so == 'recommend':
        question_list = Question.objects.annotate(
            num_voter=Count('voter')).order_by('-num_voter', '-create_date')
    elif so == 'popular':
        question_list = Question.objects.annotate(
            num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else: # elif so == 'recent':
        question_list = Question.objects.order_by('-create_date')

    # 조회
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목 검색
            Q(content__icontains=kw) | # 내용 검색
            Q(author__username__icontains=kw) | # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이 검색
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so}

    # context에 있는 Question 모델 데이터 question_list를
    # pybo/question_list.html 파일에 적용하여 HTML 코드로 변환한다.
    return render(request, 'pybo/question_list.html', context)

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)

