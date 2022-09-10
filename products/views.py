from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic


from .models import Product, Comment
from .forms import CommentForm

class ProductListView(generic.ListView):
    # model = Product
    template_name = 'products/product_list.html'
    queryset = Product.objects.filter(active=True)
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    queryset = Product.objects.filter(active=True)
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm


        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    # template_name = 'products/product_list.html'

    def get_success_url(self):
        return reverse('product:detail', args=[self.kwargs['pk']])

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        product = get_object_or_404(Product, id=self.kwargs['pk'])
        obj.product = product
        obj.save()
        return super(CommentCreateView, self).form_valid(form)




