from django import forms
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import CouponForm

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponForm(request.POST)
    if form.is_valid():
        try:
            coupon = Coupon.objects.get(
                active=True, 
                code__iexact=form.cleaned_data['code'],
                valid_from__lte=now,
                valid_to__gte=now,)
            request.session['coupon_id'] = coupon.id
        except Coupon.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')
