from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from order.forms import RegisterForm as OrderForm

# Create your views here.

class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    # context_object_name = 'product_list'
class ProductCreate(FormView):
    template_name = 'register_product.html'
    form_class = RegisterForm
    success_url = '/product/'
class ProductDetail(DetailView):
    template_name = 'product_detail.html'
    queryset = Product.objects.all()
    context_object_name = 'product'
    
    # 원하는 데이터를 넣을 수 있는 함수 제공
    def get_context_data(self, **kwargs):
        # detailview가 자동으로 전달해주는 데이터를 먼저 만들어주고 나서
        context = super().get_context_data(**kwargs)
        # 내가 원하는 데이터를 추가
        context['form'] = OrderForm(self.request)
        return context