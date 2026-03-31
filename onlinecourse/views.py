from django.shortcuts import render, get_object_or_404
from .models import Question, Choice, Submission


def submit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        selected_choice_id = request.POST.get("choice")
        selected_choice = get_object_or_404(Choice, pk=selected_choice_id)

        # Save submission
        Submission.objects.create(
            question=question,
            selected_choice=selected_choice
        )

        return show_exam_result(request, question.id)

    return render(request, "onlinecourse/course_details_bootstrap.html", {"question": question})


def show_exam_result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = question.choice_set.all()

    correct_choices = choices.filter(is_correct=True)
    selected_choice_id = request.POST.get("choice")

    score = 0
    if selected_choice_id:
        selected_choice = get_object_or_404(Choice, pk=selected_choice_id)
        if selected_choice in correct_choices:
            score = 100

    context = {
        "question": question,
        "choices": choices,
        "score": score,
    }

    return render(request, "onlinecourse/course_details_bootstrap.html", context)
