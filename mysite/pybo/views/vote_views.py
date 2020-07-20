from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Question, Answer


@login_required(login_url='common:login')
def vote_question(request, question_id):
    """
    pybo Upvote a question
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user == question.author:
        messages.error(request, 'Cannot upvote own question')
    else:
        question.voter.add(request.user)
    return redirect('pybo:detail', question_id=question.id)


def vote_answer(request, answer_id):
    """
    pybo Upvote answer
    """
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user == answer.author:
        messages.error(request, 'Cannot upvote own answer')
    else:
        answer.voter.add(request.user)
    return redirect('pybo:detail', question_id=answer.question.id)