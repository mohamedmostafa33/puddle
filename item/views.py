from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewItemForm, EditItemForm, ReviewForm
from .models import Category, Item, Cart, CartItem, Review


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    reviews = Review.objects.filter(item=item)
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.item = item
                review.user = request.user
                review.save()
                messages.success(request, 'Your review has been posted!')
                return redirect('item:detail', pk=item.pk)
        else:
            messages.error(request, 'You must be logged in to post a review!')
            return redirect('core:login') 
    else:
        form = ReviewForm()

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
        'reviews': reviews, 
        'form': form 
    })

@login_required
def update_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your review has been updated!')
            return redirect('item:detail', pk=review.item.pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, 'item/update_review.html', {
        'form': form,
        'review': review,
    })

@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id, user=request.user)
    item_pk = review.item.pk
    review.delete()
    
    messages.success(request, 'Your review has been deleted!')
    return redirect('item:detail', pk=item_pk)  

@login_required
def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    # Check if item is sold
    if item.is_sold:
        messages.error(request, 'This item is already sold!')
        return redirect('item:detail', pk=item_id)
    
    # Check if user is trying to add their own item
    if item.created_by == request.user:
        messages.error(request, 'You cannot add your own item to cart!')
        return redirect('item:detail', pk=item_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        messages.success(request, f'{item.name} quantity updated in cart!')
    else:
        messages.success(request, f'{item.name} added to cart successfully!')

    return redirect('item:cart_detail')  

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all() 
    return render(request, 'item/cart_detail.html', {'cart': cart, 'cart_items': cart_items})

@login_required
def remove_from_cart(request, item_id):
    cart = Cart.objects.get(user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, item_id=item_id)
    item_name = cart_item.item.name
    cart_item.delete()
    
    messages.success(request, f'{item_name} removed from cart!')
    return redirect('item:cart_detail')  


@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            
            messages.success(request, f'{item.name} has been listed successfully!')
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            
            messages.success(request, f'{item.name} has been updated successfully!')
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item_name = item.name
    item.delete()
    
    messages.success(request, f'{item_name} has been deleted successfully!')
    return redirect('dashboard:index')
