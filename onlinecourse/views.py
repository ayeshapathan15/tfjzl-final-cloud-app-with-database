from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Submission


# ✅ Course list (HOME PAGE)
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'onlinecourse/course_list_bootstrap.html', {'courses': courses})


# ✅ Course detail (LESSONS + EXAM PAGE)
def course_detail(request, course_id):
    course = Course.objects.get(pk=course_id)
    return render(request, 'onlinecourse/bootstrap.html', {'course': course})


# ✅ Submit exam
def submit(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    enrollment, created = Enrollment.objects.get_or_create(
        user=user,
        course=course
    )

    submission = Submission.objects.create(enrollment=enrollment)

    choices = extract_answers(request)
    submission.choices.set(choices)

    return HttpResponseRedirect(
        reverse('onlinecourse:exam_result', args=(course.id, submission.id,))
    )


# ✅ Extract answers
def extract_answers(request):
    submitted_answers = []

    for key in request.POST:
        if key.startswith('choice'):
            value = request.POST[key]
            choice_id = int(value)
            submitted_answers.append(choice_id)

    return submitted_answers


# ✅ Show result
def show_exam_result(request, course_id, submission_id):
    context = {}

    course = get_object_or_404(Course, pk=course_id)
    submission = Submission.objects.get(id=submission_id)

    choices = submission.choices.all()

    total_score = 0

    for choice in choices:
        if choice.is_correct:
            total_score += choice.question.grade

    context['course'] = course
    context['grade'] = total_score
    context['choices'] = choices

    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)