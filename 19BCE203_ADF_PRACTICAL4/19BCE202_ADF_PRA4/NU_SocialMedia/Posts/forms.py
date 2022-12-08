from django import forms  
class PostForm(forms.Form): 
    Post_title=forms.CharField(label="Enter post title",max_length=10)
    Post_Content=forms.CharField(label="Enter post content", max_length = 100)
    Post_Image=forms.ImageField()
