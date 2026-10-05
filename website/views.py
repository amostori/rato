from django.shortcuts import get_object_or_404, render

from website.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')

    context = {
        'posts': posts,
        'featured_posts': featured_posts
    }
    return render(request, 'home.html', context)

def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category=category_id, status='Published')
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)

def blog(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog
    }
    return render(request, 'blog.html', context)