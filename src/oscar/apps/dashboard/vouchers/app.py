
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class VoucherDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    list_view = get_class('dashboard.vouchers.views', 'VoucherListView')
    create_view = get_class('dashboard.vouchers.views', 'VoucherCreateView')
    update_view = get_class('dashboard.vouchers.views', 'VoucherUpdateView')
    delete_view = get_class('dashboard.vouchers.views', 'VoucherDeleteView')
    stats_view = get_class('dashboard.vouchers.views', 'VoucherStatsView')

    def get_urls(self):
        urls = [
            path('', self.list_view.as_view(), name='voucher-list'),
            path('create/', self.create_view.as_view(),
                name='voucher-create'),
            path('update/<int:pk>/', self.update_view.as_view(),
                name='voucher-update'),
            path('delete/<int:pk>/', self.delete_view.as_view(),
                name='voucher-delete'),
            path('stats/<int:pk>/', self.stats_view.as_view(),
                name='voucher-stats'),
        ]
        return self.post_process_urls(urls)


application = VoucherDashboardApplication()
