
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class ShippingDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff']

    weight_method_list_view = get_class(
        'dashboard.shipping.views', 'WeightBasedListView')
    weight_method_create_view = get_class(
        'dashboard.shipping.views', 'WeightBasedCreateView')
    weight_method_edit_view = get_class(
        'dashboard.shipping.views', 'WeightBasedUpdateView')
    weight_method_delete_view = get_class(
        'dashboard.shipping.views', 'WeightBasedDeleteView')
    # This doubles as the weight_band create view
    weight_method_detail_view = get_class(
        'dashboard.shipping.views', 'WeightBasedDetailView')
    weight_band_edit_view = get_class(
        'dashboard.shipping.views', 'WeightBandUpdateView')
    weight_band_delete_view = get_class(
        'dashboard.shipping.views', 'WeightBandDeleteView')

    def get_urls(self):
        urlpatterns = [
            path('weight-based/', self.weight_method_list_view.as_view(),
                name='shipping-method-list'),
            path('weight-based/create/', self.weight_method_create_view.as_view(),
                name='shipping-method-create'),
            path('weight-based/<int:pk>/', self.weight_method_detail_view.as_view(),
                name='shipping-method-detail'),
            path('weight-based/<int:pk>/edit/', self.weight_method_edit_view.as_view(),
                name='shipping-method-edit'),
            path('weight-based/<int:pk>/delete/', self.weight_method_delete_view.as_view(),
                name='shipping-method-delete'),
            path('weight-based/<int:method_pk>/bands/<int:pk>/', self.weight_band_edit_view.as_view(),
                name='shipping-method-band-edit'),
            path('weight-based/<int:method_pk>/bands/<int:pk>/delete/', self.weight_band_delete_view.as_view(),
                name='shipping-method-band-delete'),
        ]
        return self.post_process_urls(urlpatterns)


application = ShippingDashboardApplication()
