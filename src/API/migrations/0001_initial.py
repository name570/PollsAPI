# Generated by Django 4.0 on 2021-12-23 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_name', models.CharField(max_length=200, verbose_name='Название опроса')),
                ('poll_start_dt', models.DateField(verbose_name='Дата начала опроса')),
                ('poll_end_dt', models.DateField(verbose_name='Дата окончания опроса')),
                ('poll_description', models.TextField(verbose_name='Описание опроса')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Текст вопроса')),
                ('question_type', models.CharField(choices=[('TX', 'Text'), ('OC', 'OneChoice'), ('MC', 'ManyChoices')], max_length=2)),
                ('poll_relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.poll')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200, verbose_name='Идентификатор пользователя')),
                ('answer_text', models.TextField(verbose_name='Текст ответа')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.question')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]