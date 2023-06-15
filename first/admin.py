from django.contrib import admin
from .models import Student, Course, Topic, Subtopic, Question, Progress, Content, Assessment


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'username')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Subtopic)
class SubtopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question')


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'question', 'score')


@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_path')


@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'assessment_name')
