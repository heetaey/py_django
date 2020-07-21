from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question


def index(request):
    """
    Load pybo list
    """

    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '') # Keyword for searching
    question_list = Question.objects.order_by('-create_date')
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |  # Search subject
            Q(content__icontains=kw) |  # Search content
            Q(author__username__icontains=kw) |  # Search the Author
            Q(answer__author__username__icontains=kw)  # Search the author's answer
        ).distinct()

    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    """
    Load details
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)