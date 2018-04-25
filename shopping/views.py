from django.shortcuts import render
from shopping.models import Products, Reviews
from shopping.forms import ReviewForm




def item(request, product_id):
    
    avgreview = 0

    product = Products.objects.get(id = product_id)
    reviews = Reviews.objects.filter(product=product_id)
    for review in reviews:
        avgreview += review.stars
    
    avgreview = int(avgreview / reviews.count())
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Reviews(title=form.cleaned_data['title'], body=form.cleaned_data['body'], 
                             product=Products.objects.get(id = product_id), stars=form.cleaned_data['stars'])
            review.save()
    else:
               
       
        form = ReviewForm()
    context = {
        "product": product,
        "reviews": reviews,
        "form": form,
        "avgreview": avgreview
        }
    return render(request, "shopping/item.html", context)


# Create your views here.
def index(request, category='all'):
    
    if category == 'all':
        products = Products.objects.all()
    elif category == 'SC':
        products = Products.objects.filter(category='SC')
    elif category == 'PR':
        products = Products.objects.filter(category='PR')
    elif category == 'SB':
        products = Products.objects.filter(category='SB')
        

    context = {
        "products": products

    }

    return render(request, 'shopping/index.html', context)


def about(request):
    return render(request, 'shopping/about.html')

