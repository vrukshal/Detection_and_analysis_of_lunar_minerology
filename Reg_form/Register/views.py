from django.shortcuts import render

# Create your views here.

from django.views.generic import CreateView
from .models import user_details
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import UserForm
from django.urls import reverse_lazy
from django.shortcuts import render

# class ContactCreate(CreateView):
#     model = Contact
#     fields = {'name', 'email', 'address', 'phone'}
#     template_name = "contact_create.html"
#     success_url = reverse_lazy('Profile_list')

class userCreate(CreateView):
    model = user_details
    # form_class=UserForm
    fields = {'name', 'email', 'address', 'phone', 'password', 'gender'}
    template_name="usercreate.html"
    # context_object_name ="users"
    success_url = reverse_lazy('userlist')

class userList(ListView):
    model = user_details
    template_name="userlist.html"
    context_object_name ="users"

class userDetail(DetailView):
    model = user_details
    template_name="userdetail.html"
    context_object_name ="users"

class userUpdate(UpdateView):
    model = user_details
    # form_class=UserForm
    fields = '__all__'
    template_name="userupdate.html"
    context_object_name ="users"
    success_url = reverse_lazy('userlist')


class userDelete(DeleteView):
    model = user_details
    template_name="userdelete.html"
    context_object_name ="users"
    success_url = reverse_lazy('userlist')

