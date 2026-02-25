from .models import Product
from decimal import Decimal

CART_SESSION_KEY = 'cart'

class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.setdefault(CART_SESSION_KEY, {})

    def add(self, product, quantity=1, override=False):
        key = str(product.id)
        if key not in self.cart:
            self.cart[key] = {'quantity': 0, 'price': str(product.price)}
        if override:
            self.cart[key]['quantity'] = quantity
        else:
            self.cart[key]['quantity'] += quantity
        self.save()

    def remove(self, product):
        key = str(product.id)
        if key in self.cart:
            del self.cart[key]
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['total_price'] = Decimal(item['price']) * item['quantity']
            yield item

    def get_total(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[CART_SESSION_KEY]
        self.save()

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())