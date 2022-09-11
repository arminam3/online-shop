
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

    def save(self):
        """
        Save Changes In Session
        """
        self.session.modified = True


