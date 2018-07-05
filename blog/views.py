from .models import Category, BlogPost


def view_content(request):
    posts = BlogPost.objects.all()
    post_contents = list(posts.values('title', 'slug'))
    # pprint.pprint(post_contents)
    for values in post_contents:
        print(values)
    # return post_contents


def view_category(request):
    categories = Category.objects.all()
    categories_content = categories.values('name')
    category_name = []
    # print(categories_content)
    for values in categories_content:
        # print(values)
        # print(values['name'])
        category_name += [values['name']]
    print(category_name)
    return category_name
