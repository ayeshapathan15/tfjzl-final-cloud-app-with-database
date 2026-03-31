from django.contrib import admin
from .models import Question, Choice, Submission


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    search_fields = ['question_text']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question', 'votes')


class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('question', 'selected_choice', 'submitted_at')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Submission, SubmissionAdmin)
