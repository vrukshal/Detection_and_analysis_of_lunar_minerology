from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from requests import request

# Create your views here.
from .models import post_details,comment
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import PostForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.template.loader import render_to_string

# class ContactCreate(CreateView):
#     model = Contact
#     fields = {'name', 'email', 'address', 'phone'}
#     template_name = "contact_create.html"
#     success_url = reverse_lazy('Profile_list')

class postCreate(CreateView):
    model = post_details
    # form_class=UserForm
    fields = ['Post_owner','Post_title','Post_Content','Post_Image']
    
    template_name="postcreate.html"
    # context_object_name ="users"
    success_url = reverse_lazy('postlist')

class postList(ListView):
    model = post_details
    template_name="postlist.html"
    context_object_name ="post"
    

def showcomment(request,pk):
    a1=post_details.objects.filter(id=pk)
    a2=comment.objects.filter(id=pk)
    return render(request,"showcomment.html",{"a1":a1,"a2":a2})
    
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(postList, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the Baklawa
    #     context['comment'] = comment.objects.filter(container=1)
    #     return context

class postUpdate(UpdateView):
    model = post_details
    # form_class=UserForm
    fields = '__all__'
    template_name="postupdate.html"
    context_object_name ="post"
    success_url = reverse_lazy('postlist')


def postlikeupdate(request,pk):
    post=post_details.objects.get(id=pk)
    post.Post_like +=1
    post.save()
    return redirect('postlist')

def postcomment(req,pk):
    if req.method == 'POST':
        cmt = req.POST['comment']
        a=post_details.objects.get(id=pk)
        post = comment(id=None,container=a,value=cmt,comment_owner=a.Post_owner)
        post.save()
        return redirect('postlist')



class postDelete(DeleteView):
    model = post_details
    template_name="postdelete.html"
    context_object_name ="post"
    success_url = reverse_lazy('postlist')




# create one function based view to increament like for that post and redirect to same page
