from products.models import Product


class Cart:
    def __init__(self, request):
        """
        Inisialize The Cart
        """
        self.request = request
        self.session = request.session

        cart = request.session.get('cart')

        if not cart:
            cart = request.session['cart'] = {}

        self.cart = cart

    def add(self, product, quantity=1):
        """
        Add A Product To Cart OR Increase It's quantity
        """
        product_id = str(product.id)
        cart = self.cart

        if not product_id in cart:
            cart[product_id] = {'quantity': quantity}
        else:
            cart[product_id]['quantity'] += quantity

        self.save()

    def remove(self, product):
        """
        Remove a product from cart
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]

        self.save()


    def save(self):
        """
        Save Changes In Session
        """
        self.session.modified = True

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product_obj'] = product

        for item in cart.values():
            yield item

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        # total = 0
        #
        # for product in products:
        #     quantity = self.cart[str(product.id)]['quantity']
        #     total += product.price * quantity
        # return total
        return sum(product.price for product in products)
