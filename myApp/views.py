from django.urls import reverse_lazy
from django.views import generic
from .models import Project
from .forms import ProjectForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(generic.ListView):
    model = Project
    context_object_name = 'projects'
    template_name = "myApp/index.html"
    

class AddProjectView(LoginRequiredMixin, generic.CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('home')
    template_name = "myApp/add_project.html"
    


class DeleteProjectView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy('home')
    template_name = "myApp/delete_project.html"

    def form_valid(self, form):
      messages.success(self.request, "Project deleted successfully!")
      return super().form_valid(form)  


class EditProjectView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('home')
    template_name = "myApp/edit_project.html"

