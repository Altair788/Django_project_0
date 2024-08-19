from django.urls import path

from students.views import students_list

app_name = 'students'

urlpatterns = [
    path('', students_list)
]
