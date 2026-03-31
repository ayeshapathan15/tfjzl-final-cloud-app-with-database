from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [

    path('', views.course_list, name='index'),

    path('<int:course_id>/', views.course_detail, name='course_details'),

    # ✅ ADD THIS LINE (YOU MISSED THIS)
    path('<int:course_id>/submit/', views.submit, name='submit'),

    path(
        'course/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='exam_result'
    ),
]