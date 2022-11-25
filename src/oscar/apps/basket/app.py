from django.contrib.auth.decorators import login_required

from oscar.core.application import Application
from oscar.core.loading import get_class
from django.urls import path


class BasketApplication(Application):
    name = 'basket'
    summary_view = get_class('basket.views', 'BasketView')
    saved_view = get_class('basket.views', 'SavedView')
    add_view = get_class('basket.views', 'BasketAddView')
    add_voucher_view = get_class('basket.views', 'VoucherAddView')
    remove_voucher_view = get_class('basket.views', 'VoucherRemoveView')

    def get_urls(self):
        urls = [
            path('', self.summary_view.as_view(), name='summary'),
            path('add/<int:pk>/', self.add_view.as_view(), name='add'),
            path('vouchers/add/', self.add_voucher_view.as_view(),
                name='vouchers-add'),
            path('vouchers/<int:pk>/remove/', self.remove_voucher_view.as_view(), name='vouchers-remove'),
            path('saved/', login_required(self.saved_view.as_view()),
                name='saved'),
        ]
        return self.post_process_urls(urls)


application = BasketApplication()
