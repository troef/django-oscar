
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class OrdersDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]
    permissions_map = {
        'order-list': (['is_staff'], ['partner.dashboard_access']),
        'order-stats': (['is_staff'], ['partner.dashboard_access']),
        'order-detail': (['is_staff'], ['partner.dashboard_access']),
        'order-detail-note': (['is_staff'], ['partner.dashboard_access']),
        'order-line-detail': (['is_staff'], ['partner.dashboard_access']),
        'order-shipping-address': (['is_staff'], ['partner.dashboard_access']),
    }

    order_list_view = get_class('dashboard.orders.views', 'OrderListView')
    order_detail_view = get_class('dashboard.orders.views', 'OrderDetailView')
    shipping_address_view = get_class('dashboard.orders.views',
                                      'ShippingAddressUpdateView')
    line_detail_view = get_class('dashboard.orders.views', 'LineDetailView')
    order_stats_view = get_class('dashboard.orders.views', 'OrderStatsView')

    def get_urls(self):
        urls = [
            path('', self.order_list_view.as_view(), name='order-list'),
            path('statistics/', self.order_stats_view.as_view(),
                name='order-stats'),
            path('<slug:number>/', self.order_detail_view.as_view(), name='order-detail'),
            path('<slug:number>/notes/<int:note_id>/', self.order_detail_view.as_view(), name='order-detail-note'),
            path('<slug:number>/lines/<int:line_id>/', self.line_detail_view.as_view(), name='order-line-detail'),
            path('<slug:number>/shipping-address/', self.shipping_address_view.as_view(),
                name='order-shipping-address'),
        ]
        return self.post_process_urls(urls)


application = OrdersDashboardApplication()
