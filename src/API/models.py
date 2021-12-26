from django.db import models


# Create your models here.

class Poll(models.Model):
    poll_name = models.CharField(max_length=200, verbose_name='Название опроса')
    poll_start_dt = models.DateField(auto_now=False, verbose_name='Дата начала опроса')
    poll_end_dt = models.DateField(auto_now=False, verbose_name='Дата окончания опроса')
    poll_description = models.TextField(verbose_name='Описание опроса')

    def __str__(self):
        return self.poll_name

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Question(models.Model):
    question_text = models.TextField(verbose_name='Текст вопроса')
    poll_relation = models.ForeignKey(Poll, on_delete=models.CASCADE, null=False,
                                      verbose_name='Вопрос из опроса', related_name='poll')

    class QuestionType(models.TextChoices):
        TEXT = 'TX', ('Text')
        ONECHOICE = 'OC', ('OneChoice')
        MANYCHOICES = 'MC', ('ManyChoices')

    question_type = models.CharField(max_length=2, choices=QuestionType.choices, verbose_name='Тип вопроса')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE, null=False,
                                    verbose_name='Идентификатор вопроса', related_name='question')
    user_id = models.CharField(max_length=200, verbose_name='Идентификатор пользователя')
    answer_text = models.TextField(verbose_name='Текст ответа')

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
