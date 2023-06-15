from django.db import models


class Student(models.Model):
    username = models.CharField(max_length=255, verbose_name='Имя пользователя')
    password = models.CharField(max_length=255, verbose_name='Пароль')

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'

    def __str__(self):
        return self.username


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(max_length=255, blank=True, verbose_name='Краткое описание')
    what_you_will_learn = models.CharField(max_length=255, verbose_name='Навыки, получаемые в курсе')
    teaser_video_link = models.URLField(max_length=255, verbose_name='Ссылка на видео-анонс курса')
    course_icon = models.CharField(max_length=255, verbose_name='Путь к иконке курса')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    name = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(max_length=1024, blank=True, verbose_name='Краткое описание')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return self.name


class Subtopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    name = models.CharField(max_length=255, verbose_name='Название')
    short_description = models.TextField(max_length=255, blank=True, verbose_name='Краткое описание')

    class Meta:
        verbose_name = 'Подтема'
        verbose_name_plural = 'Подтемы'

    def __str__(self):
        return self.name


class Question(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, verbose_name='Тема')
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, verbose_name='Подтема')
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE, verbose_name='оценивающий тест')
    question = models.CharField(max_length=255, verbose_name='Вопрос')
    correct_option = models.CharField(max_length=255, verbose_name='Правильный вариант')
    option_a = models.CharField(max_length=255, verbose_name='Вариант A')
    option_b = models.CharField(max_length=255, verbose_name='Вариант B')
    option_c = models.CharField(max_length=255, verbose_name='Вариант C')
    option_d = models.CharField(max_length=255, verbose_name='Вариант D')
    option_e = models.CharField(max_length=255, verbose_name='Вариант E')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question


class Progress(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    selected_option = models.CharField(max_length=255, verbose_name='Выбранный вариант')
    score = models.IntegerField(verbose_name='Оценка')

    class Meta:
        verbose_name = 'Прогресс'
        verbose_name_plural = 'Прогресс'

    def __str__(self):
        return f"Progress ID: {self.id}"


class Content(models.Model):
    subtopic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, verbose_name='Подтема')
    file_path = models.CharField(max_length=255, verbose_name='Путь к файлу')

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'

    def __str__(self):
        return self.file_path


class Assessment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, verbose_name='Контент')
    assessment_name = models.CharField(max_length=255, verbose_name='Название оценившего теста')

    class Meta:
        verbose_name = 'Оценивающий тест'
        verbose_name_plural = 'Оценивающие тесты'

    def __str__(self):
        return self.assessment_name
