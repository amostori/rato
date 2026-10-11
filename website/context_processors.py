from website.models import Category
from assignments.models import SocialLink
from django.conf import settings

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    return dict(social_links=SocialLink.objects.all())

def get_tiny_api(request): 
    return dict(tiny_api=settings.TINYMCE_API_KEY)