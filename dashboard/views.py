from django.shortcuts import get_object_or_404, redirect, render
from dashboard.forms import CategoryForm, AddUserForm, BlogPostForm
from website.models import Blog, Category
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.contrib import messages


@login_required
@staff_member_required
def dashboard(request):
    category_count = Category.objects.count()
    blogs_count = Blog.objects.count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count
    }
    return render(request, 'dashboard.html', context)


@login_required
@staff_member_required
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)



@login_required
@staff_member_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dodano nową kategorię {form.cleaned_data.get("category_name")}!')
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'add_category.html', context)

@login_required
@staff_member_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Zaktualizowano kategorię {form.cleaned_data.get("category_name")}!')
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'edit_category.html', context)

@login_required
@staff_member_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.warning(request, f'Usunięto kategorię {category.category_name}!')
    return redirect('categories')

@login_required
@staff_member_required
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'users.html', context)

@login_required
@staff_member_required
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Dodano nowego użytkownika: {form.cleaned_data.get("username")}!')
            return redirect('users')
    form = AddUserForm()
    context = {
        'form': form
    }
    return render(request, 'add_user.html', context)

@login_required
@staff_member_required
def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = AddUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Zaktualizowano dane użytkownika: {form.cleaned_data.get("username")}!')
            return redirect('users')
    form = AddUserForm(instance=user)
    context = {
        'form': form,
        'user': user
    }
    return render(request, 'edit_user.html', context)

@login_required
@staff_member_required
def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.warning(request, f'Usunięto użytkownika: {user.username}!')
    return redirect('users')

@login_required
@staff_member_required
def posts(reqest):
    posts = Blog.objects.all()
    context = {
        'posts': posts
    }
    return render(reqest, 'posts.html', context)

@login_required
@staff_member_required
def add_post(request):
    if request.method == 'POST':
        # by przesyłać formularz wraz z plikiem nalezy ustawić request.FILES oraz
        # w html, w tagu formularza ustawić enctype="multipart/form-data"
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save() # zapisujemy do bazy by dostępny był id
            title = form.cleaned_data.get('title')
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            messages.success(request, f'Dodano post {post.title}!')
            return redirect('posts')
    form = BlogPostForm()
    context = {
        'form': form
    }
    return render(request, 'add_post.html', context)

@login_required
@staff_member_required
def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            title = form.cleaned_data.get('title')
            post.slug = slugify(title) + '-'+str(post.id)
            post.save()
            messages.success(request, f'Zaktualizowano post {post.title}!')
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form': form,
        'post': post
    }
    return render(request, 'edit_post.html', context)

@login_required
@staff_member_required
def delete_post(request, pk):
    
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.warning(request, f'Usunięto post {post.title}!')
        return redirect('posts')
    
    return render(request, 'delete_post.html', {'post': post})