
from typing import Any
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.shortcuts import redirect,render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from .forms import *
from .models import *
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class CustomLoginView(LoginView):
    template_name="login.html"
    fields='__all__'
    
    def get_success_url(self):
        return reverse_lazy('tasklist')
    
class register(FormView):
    template_name="register.html"
    form_class=CustomUserForm
    context_object_name='form'
    redirect_authenticated_user=True
    success_url=reverse_lazy('tasklist')
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
            messages.success(self.request, f"user addedsuccessfully")
        return super(register,self).form_valid(form)
    def get(self,*args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasklist')
        return super(register,self).get(*args, **kwargs)
class TaskList(LoginRequiredMixin,ListView):
    model= Task
    template_name='task_list.html'
    context_object_name='task'
    # paginate_by=4
    ordering=['-create']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] =context['task'].filter(user=self.request.user) 
        context['id']=context['task'].filter(complete=False).count()
        search_input=self.request.GET.get('search-area') or ''
        if search_input:
            context['task']=context['task'].filter(title__icontains=search_input)
        context['search_input']=search_input
        return context
    
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model=Task
    template_name='task_detail.html'
    context_object_name='task'
class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    context_object_name='form'
    template_name='task_create.html'
    success_url=reverse_lazy('tasklist')
    form_class=TaskForm
    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request, f"Task added successfully")
        return super(TaskCreate,self).form_valid(form)
class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    form_class=TaskForm
    template_name='task_create.html'
    context_object_name='task'
    success_url=reverse_lazy('tasklist')
    def form_valid(self, form):
        messages.success(self.request, f"Task edited successfully")
        return super().form_valid(form)
class TaskDelete(SuccessMessageMixin,DeleteView):
    model=Task
    form_class=TaskForm
    template_name='task_delete.html'
    context_object_name='task'
    success_url=reverse_lazy('tasklist')
    success_message = "deleted successfully"
    def form_valid(self, form):
        messages.success(self.request, f"Task edited successfully")
        return super().form_valid(form)
