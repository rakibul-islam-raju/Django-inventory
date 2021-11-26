from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
from django.views.generic import View, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin

from .models import *
from .forms import *

from core.models import Product
from sell.models import SellProductItem, Customer
from sell.forms import SellProductItemForm, SellForm, CustomerForm


# class AllOrdersView(LoginRequiredMixin,
#                     UserPassesTestMixin,
#                     ListView):
#     model = Order
#     template_name = 'order/order_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["title"] = 'Order List'
#         context["orders"] = Order.objects.all().order_by('order_status')
#         return context

#     def test_func(self):
#         if self.request.user.is_staff:
#             return True
#         return False


class OrderListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Order
    template_name = "order/order_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Order List"
        if self.request.user.is_customer:
            context["orders"] = Order.objects.filter(user=self.request.user).order_by(
                "order_status"
            )
        else:
            context["orders"] = Order.objects.all().order_by("order_status")
        return context

    def test_func(self):
        if self.request.user.is_customer or self.request.user.is_staff:
            return True
        return False


class OrderCreateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs["product_id"])
        form = OrderForm(initial={"quantity": product.quantity})
        context = {
            "form": form,
            "product": product,
            "title": "Create New Order",
            "orders": Order.objects.filter(user=self.request.user),
        }
        return render(self.request, "order/create_order.html", context)

    def post(self, *args, **kwargs):
        form = OrderForm(self.request.POST or None)

        if form.is_valid():
            quantity = form.cleaned_data.get("quantity")
            product = get_object_or_404(Product, pk=self.kwargs["product_id"])
            new_order = Order(
                quantity=quantity, product=product, user=self.request.user
            )
            new_order.save()
            messages.success(self.request, "Order created successfully")
            return redirect("./")
        else:
            return redirect("./")

    def test_func(self):
        if self.request.user.is_customer:
            return True
        return False


class OrderUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Order
    form_class = OrderForm
    template_name = "order/create_order.html"
    success_url = "order:order-list"
    success_message = "Order was updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Edit Order"
        context["orders"] = Order.objects.filter(user=self.request.user)
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_customer:
            return True
        return False


class OrderDeleteView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView
):
    model = Order
    template_name = "delete.html"
    success_url = "order:order-list"
    success_message = "Order was deleted successfully"

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def test_func(self):
        if self.request.user.is_customer:
            current_user = self.get_object()
            if self.request.user == current_user.user:
                return True
        return False


class SellOrderItem(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, CreateView
):
    model = SellProductItem
    template_name = "order/order_sell.html"
    form_class = SellProductItemForm
    success_url = "sell:sales"
    success_message = "Order was created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = SellProductItem.objects.all()
        return context

    def get_success_url(self, **kwargs):
        return reverse(self.success_url)

    def get(self, *args, **kwargs):
        order_instance = get_object_or_404(Order, pk=self.kwargs["pk"])
        customer = Customer.objects.get(phone=order_instance.user.phone)
        sale_item_form = SellProductItemForm(
            initial={
                "product": order_instance.product,
                "price": order_instance.product.sell_price,
                "quantity": order_instance.quantity,
            }
        )
        sale_form = SellForm(initial={"customer": customer})

        context = {
            "sale_item_form": sale_item_form,
            "customer": customer,
            "sale_form": sale_form,
        }
        return render(self.request, "order/order_sell.html", context)

    def post(self, *args, **kwargs):
        order_instance = get_object_or_404(Order, pk=self.kwargs["pk"])
        product_instance = get_object_or_404(Product, pk=order_instance.product.pk)
        customer = Customer.objects.get(phone=order_instance.user.phone)

        sale_item_form = SellProductItemForm(self.request.POST)
        sale_form = SellForm(self.request.POST)

        print(sale_form)

        if sale_item_form.is_valid():
            if sale_form.is_valid():
                quantity = sale_item_form.cleaned_data.get("quantity")

                if quantity <= product_instance.quantity:
                    new_qntty = product_instance.quantity - quantity
                    product_instance.quantity = new_qntty
                else:
                    messages.error(self.request, "Insufficient product quantity")
                    return redirect("./")

                sale_item = sale_item_form.save(commit=False)
                sale = sale_form.save(commit=False)
                sale.added_by = self.request.user
                sale.save()
                sale_item.sell = sale
                sale_item.save()
                product_instance.save(update_fields=["quantity"])

                order_instance.order_status = True
                order_instance.save()

                messages.success(self.request, "Order created successfully")
                return redirect("order:order-list")
            else:
                print("invalid...")
                print(
                    "sale_form",
                    sale_form.errors,
                )
                messages.warning(self.request, "Invalid form data")
                return redirect("./")
        else:
            print(
                "sale_item_form",
                sale_item_form.errors,
            )

            messages.warning(self.request, "Invalid form data")
            return redirect("./")

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False
