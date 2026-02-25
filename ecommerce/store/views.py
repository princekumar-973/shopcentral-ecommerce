from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Category, Order, OrderItem
from .cart import Cart


def product_list(request):
    products      = Product.objects.filter(available=True)
    categories    = Category.objects.all()
    category_slug = request.GET.get('category')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'store/product_list.html', {
        'products':   products,
        'categories': categories
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})


def home(request):
    featured_products = Product.objects.filter(available=True)[:8]
    categories        = Category.objects.all()
    return render(request, 'store/home.html', {
        'featured_products': featured_products,
        'categories':        categories,
    })


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart.html', {'cart': cart})


@login_required
def cart_add(request, product_id):
    cart     = Cart(request)
    product  = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart.add(product, quantity)
    return redirect('store:cart_detail')


def cart_remove(request, product_id):
    cart    = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('store:cart_detail')


@login_required
def place_order(request):
    cart = Cart(request)

    # If cart is empty → go back to cart page
    if not cart:
        return redirect('store:cart_detail')

    if request.method == 'POST':
        payment_method = request.POST.get('payment', 'cod')

        # Get address from form fields
        address = request.POST.get('address', '').strip()
        city    = request.POST.get('city', '').strip()
        state   = request.POST.get('state', '').strip()
        pincode = request.POST.get('pincode', '').strip()

        # Validate — all fields must be filled
        if not address or not city or not state or not pincode:
            return render(request, 'store/cart.html', {
                'cart':  cart,
                'error': 'Please fill in all delivery address fields before placing order.'
            })

        # Create Order in database
        order = Order.objects.create(
            user           = request.user,
            payment_method = payment_method,
            total_amount   = cart.get_total(),
            address        = address,
            city           = city,
            state          = state,
            pincode        = pincode,
        )

        # Save each cart item as OrderItem
        for item in cart:
            OrderItem.objects.create(
                order    = order,
                product  = item['product'],
                quantity = item['quantity'],
                price    = item['price'],
            )

        # Save address to profile for next time
        request.user.profile.address = address
        request.user.profile.city    = city
        request.user.profile.state   = state
        request.user.profile.pincode = pincode
        request.user.profile.save()

        # Clear the cart
        cart.clear()

        return redirect('store:order_success', order_id=order.id)

    return redirect('store:cart_detail')

@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_success.html', {'order': order})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/my_orders.html', {'orders': orders})