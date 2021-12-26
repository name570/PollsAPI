from rest_framework import serializers
from .models import Poll, Question, Answer


class PollModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ['poll_name', 'poll_description']


class QuestionSerializer(serializers.ModelSerializer):
    poll_relation = PollModelSerializer()

    class Meta:
        model = Question
        fields = ['question_text', 'poll_relation']


class AnswerSerializer(serializers.ModelSerializer):
    question_id = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ['answer_text', 'question_id']


class PollSerializer(serializers.Serializer):
    poll_name = serializers.CharField(max_length=200)
    poll_description = serializers.CharField()
