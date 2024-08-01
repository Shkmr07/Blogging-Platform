from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .forms import signUpForm,createPost,commentPost
from django.contrib.auth.models import User
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Post
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm
def index(request):
    return render(request,'Blogs/index.html',context=None)

def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('index')
    else: form = signUpForm()
    return render(request,'Blogs/signup.html',{'form': form})

def login(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request,user)
            return redirect('post_list')
        else: return redirect('signup')

    else: form = AuthenticationForm()
    return render(request,'Blogs/login.html',{'form':form})

def logout(request):

    if request.method == 'POST':
        django_logout(request)
        return redirect('index')
    
    return render(request,'Blogs/logout.html',context=None)


@login_required(login_url='/blogs/login/')
def post_list(request):
    posts = Post.objects.filter(author = request.user)

    return render(request,'Blogs/postlist.html',{'posts':posts})

@login_required(login_url='/blogs/login/')
def create_post(request):
    if request.method == "POST":
        form = createPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
        
    else: form = createPost()
    return render(request,'Blogs/createpost.html',{'form':form})

@login_required(login_url='/blogs/login/')
def update_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = createPost(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    
    else: form = createPost(instance=post)
    return render(request,'Blogs/updatepost.html',{'form':form})

@login_required(login_url='/blogs/login/')
def delete_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request,'Blogs/deletepost.html',{'post':post})
        
@login_required(login_url='/blogs/login/')
def comment_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = commentPost(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_list')
            
    else: form = commentPost()
    return render(request,'Blogs/commentpost.html',{'form':form})


@login_required(login_url='/blogs/login/')
def user_profile(request):
    detail = request.user
    return render(request,'Blogs/profile.html',{'detail':detail})
    





    








