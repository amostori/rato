from website.models import Category
from assignments.models import SocialLink


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    return dict(social_links=SocialLink.objects.all())