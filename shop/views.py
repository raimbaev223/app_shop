from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Comment
# from .forms import CartAddProductForm
from .forms import CommentForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product,
#                                 id=id,
#                                 slug=slug,
#                                 available=True)
#     products = Product.objects.get(pk=id)
#     comments = Comment.objects.filter(product=products)
#     cart_product_form = CartAddProductForm()
#     form = CommentForm()
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 name=form.cleaned_data["name"],
#                 body=form.cleaned_data["body"],
#                 product=product,
#             )
#             comment.save()
#     return render(request, 'shop/product/detail.html',
#                   {'product': product, 'cart_product_form': cart_product_form, 'comments': comments, 'form': form})
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    comments = Comment.objects.all()
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form,
                   'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form}, )

# def blog_detail(request, pk):
#     products = Product.objects.get(pk=pk)
#     comments = Comment.objects.filter(product=product)
#
#     form = CommentForm()
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = Comment(
#                 name=form.cleaned_data["name"],
#                 body=form.cleaned_data["body"],
#                 product=product,
#             )
#             comment.save()
#
#     context = {"product": product, "comments": comments, "form": form}
#     return render(request, "product/detail.html", context)
