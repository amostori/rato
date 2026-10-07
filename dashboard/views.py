from django.shortcuts import get_object_or_404, redirect, render
from dashboard.forms import CategoryForm
from website.models import Blog, Category
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    category_count = Category.objects.count()
    blogs_count = Blog.objects.count()
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count
    }
    return render(request, 'dashboard.html', context)


@login_required
def categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'categories.html', context)



@login_required
def add_category(request):
    return render(request, 'add_category.html')

@login_required
def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'edit_category.html', context)

@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')
