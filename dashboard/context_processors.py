from blog.models import Category


def return_category_details(request):
    categories = Category.objects.values('name', 'pk')
    return {
        'categories': categories
    }
