from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Student, Subject
from main.forms import StudentForm, SubjectForm


@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f"name: {name}\nemail: {email}\nmessage: {message}\n")

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)


class StudentListView(LoginRequiredMixin, PermissionRequiredMixin,ListView):
    model = Student
    permission_required = 'main.view_student'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    permission_required = 'main.view_student'


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy('main:index')
    form_class = StudentForm
    permission_required = 'main.add_student'


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    success_url = reverse_lazy('main:index')
    form_class = StudentForm
    permission_required = 'main.change_student'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
            
        return super().form_valid(form)


class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')
    permission_required = 'main.delete_student'

def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:index'))
