
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class RangeDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    list_view = get_class('dashboard.ranges.views', 'RangeListView')
    create_view = get_class('dashboard.ranges.views', 'RangeCreateView')
    update_view = get_class('dashboard.ranges.views', 'RangeUpdateView')
    delete_view = get_class('dashboard.ranges.views', 'RangeDeleteView')
    products_view = get_class('dashboard.ranges.views', 'RangeProductListView')
    reorder_view = get_class('dashboard.ranges.views', 'RangeReorderView')

    def get_urls(self):
        urlpatterns = [
            path('', self.list_view.as_view(), name='range-list'),
            path('create/', self.create_view.as_view(), name='range-create'),
            path('<int:pk>/', self.update_view.as_view(),
                name='range-update'),
            path('<int:pk>/delete/', self.delete_view.as_view(),
                name='range-delete'),
            path('<int:pk>/products/', self.products_view.as_view(),
                name='range-products'),
            path('<int:pk>/reorder/', self.reorder_view.as_view(),
                name='range-reorder'),
        ]
        return self.post_process_urls(urlpatterns)


application = RangeDashboardApplication()
