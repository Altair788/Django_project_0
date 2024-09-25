from django.shortcuts import render


# Create your views here.
def students_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        print(f"name {name}")
    return render(request, "material_list.html")
