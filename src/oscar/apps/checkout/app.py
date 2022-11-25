from django.conf import settings
from django.contrib.auth.decorators import login_required

from oscar.core.application import Application
from oscar.core.loading import get_class
from django.urls import path


class CheckoutApplication(Application):
    name = 'checkout'

    index_view = get_class('checkout.views', 'IndexView')
    shipping_address_view = get_class('checkout.views', 'ShippingAddressView')
    user_address_update_view = get_class('checkout.views',
                                         'UserAddressUpdateView')
    user_address_delete_view = get_class('checkout.views',
                                         'UserAddressDeleteView')
    shipping_method_view = get_class('checkout.views', 'ShippingMethodView')
    payment_method_view = get_class('checkout.views', 'PaymentMethodView')
    payment_details_view = get_class('checkout.views', 'PaymentDetailsView')
    thankyou_view = get_class('checkout.views', 'ThankYouView')

    def get_urls(self):
        urls = [
            path('', self.index_view.as_view(), name='index'),

            # Shipping/user address views
            path('shipping-address/', self.shipping_address_view.as_view(), name='shipping-address'),
            path('user-address/edit/<int:pk>/', self.user_address_update_view.as_view(),
                name='user-address-update'),
            path('user-address/delete/<int:pk>/', self.user_address_delete_view.as_view(),
                name='user-address-delete'),

            # Shipping method views
            path('shipping-method/', self.shipping_method_view.as_view(), name='shipping-method'),

            # Payment views
            path('payment-method/', self.payment_method_view.as_view(), name='payment-method'),
            path('payment-details/', self.payment_details_view.as_view(), name='payment-details'),

            # Preview and thankyou
            path('preview/', self.payment_details_view.as_view(preview=True),
                name='preview'),
            path('thank-you/', self.thankyou_view.as_view(),
                name='thank-you'),
        ]
        return self.post_process_urls(urls)

    def get_url_decorator(self, pattern):
        if not settings.OSCAR_ALLOW_ANON_CHECKOUT:
            return login_required
        if pattern.name.startswith('user-address'):
            return login_required
        return None


application = CheckoutApplication()
