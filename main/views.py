from django.shortcuts import render

from main.models import Student


# Create your views here.
# def index(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         message = request.POST.get("message")
#         print(f"name: {name}\nemail: {email}\nmessage: {message}\n")
#     return render(request, 'main/index.html')


def index(request):
    students_list = Student.objects.all()
    context = {
        'object_list': students_list
    }
    return render(request, 'main/index.html', context)
