from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from assignments.models import About
from website.models import Blog, Category


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    try:
        about = About.objects.get()
        # metoda get() zwraca tylko jeden obiekt. Jeśli obiekt nie istnieje 
        # lub istnieje więcej niż jeden, metoda get() zwraca wyjątek
    except:
        about = None
    context = {
        'posts': posts,
        'featured_posts': featured_posts,
        'about': about
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

def search(request):
    keyword = request.GET.get('keyword')
    # Q zapewnia zapytanie do bazy o charakterze "lub"
    # icontains - ignoring case
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
  
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)