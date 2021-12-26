from datetime import date
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Poll, Question, Answer
from .serializers import PollSerializer, AnswerSerializer

# Create your views here.


def start_page(request):
    return render(request, './start_page.html')


def get_active_polls(request):
    polls = Poll.objects.filter(poll_start_dt__lte=date.today(), poll_end_dt__gte=date.today())
    dict_item = {
        'active_polls': polls
    }
    return render(request, './active_polls.html', dict_item)


def is_poll_in_list(list_of_polls, poll):
    for item in list_of_polls:
        if item[0] == poll:
            return True
    return False


def index_of_poll(list_of_polls, poll):
    i = 0
    for item in list_of_polls:
        if item[0] == poll:
            return i
        i += 1
    return i


def get_deatiles_polls(request):
    if request.GET['user_id'] == "":
        return render(request, './polls_submitted_detailed.html')
    answers = Answer.objects.filter(user_id=request.GET['user_id'])
    polls = []
    for answer in answers:
        poll = Question.objects.get(pk=answer.question_id.id).poll_relation
        if is_poll_in_list(polls, poll):
            polls[index_of_poll(polls, poll)][1] += [[answer.question_id, answer]]
        else:
            polls += [[poll, [[answer.question_id, answer]]]]

    dict_item = {
        'polls': polls,
    }
    return render(request, './polls_submitted_detailed.html', dict_item)


def thanks_page(request):
    dict_item = {
        'user_id': request.GET['user_id']
    }
    return render(request, './thanks.html', dict_item)


def answer_questions(request):
    question_count_int = int(request.POST['question_count'])
    if question_count_int > 0:
        answer = Answer()
        answer.question_id = Question.objects.get(pk=request.POST['question'])
        answer.answer_text = request.POST['answer']
        answer.user_id = request.POST['id_user']
        answer.save()
    question_list = Question.objects.filter(poll_relation=request.POST['poll_id'])
    if len(question_list) < question_count_int + 1:
        dict_item = {
            'id_user': request.POST['id_user']
        }
        return render(request, './thanks.html', dict_item)
    else:
        dict_item = {
            'question': question_list[question_count_int],
            'question_count': question_count_int + 1,
            'id_user': request.POST['id_user'],
            'poll_id': request.POST['poll_id']
        }
        return render(request, './answer_question.html', dict_item)


def start_poll(request):
    dict_item = {
        'poll_id': request.GET['poll_id']
    }
    return render(request, './start_poll.html', dict_item)


def get_submitted_polls(request):
    if request.GET['user_id'] == "":
        return render(request, './polls_submitted.html')
    answers = Answer.objects.filter(user_id=request.GET['user_id'])
    polls = set()
    for answer in answers:
        polls.add(Question.objects.get(pk=answer.question_id.id).poll_relation)
    dict_item = {
        'polls': polls,
        'user_id': request.GET['user_id']
    }
    return render(request, './polls_submitted.html', dict_item)


def get_user_id(request):
    return render(request, './get_user_id.html')


class PollsView(APIView):
    def get(self, request):
        polls = Poll.objects.filter(poll_start_dt__lte=date.today(), poll_end_dt__gte=date.today())
        serializer = PollSerializer(polls, many=True)
        return Response({"polls": serializer.data})


class PollsWithAnswer(APIView):
    def get(self, request):
        if 'user_id' not in request.GET or request.GET['user_id'] == "":
            return Response({'detailed_polls': {}})
        answers = Answer.objects.filter(user_id=request.GET['user_id'])
        serializer = AnswerSerializer(answers, many=True)
        return Response({'detailed_polls': serializer.data})

    def post(self, request):
        answers_from = request.data['answers']
        for answer in answers_from:
            if is_answer_json_valid(answer):
                new_answer = Answer()
                new_answer.answer_text = answer['answer_text']
                new_answer.question_id = Question.objects.get(pk=answer['question_id'])
                if 'user_id' in request.data:
                    new_answer.user_id = request.data['user_id']
                new_answer.save()
            else:
                return Response({}, status=status.HTTP_400_BAD_REQUEST)
        return Response({})


def is_answer_json_valid(dict_json):
    if 'answer_text' in dict_json:
        if 'question_id' in dict_json:
            if Question.objects.filter(pk=dict_json['question_id']).count() == 1:
                return True
    return False
