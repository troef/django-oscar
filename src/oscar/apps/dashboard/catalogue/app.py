
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path, re_path


class CatalogueApplication(DashboardApplication):
    name = None

    default_permissions = ['is_staff', ]
    permissions_map = _map = {
        'catalogue-product': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-create': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-list': (['is_staff'], ['partner.dashboard_access']),
        'catalogue-product-delete': (['is_staff'],
                                     ['partner.dashboard_access']),
        'catalogue-product-lookup': (['is_staff'],
                                     ['partner.dashboard_access']),
    }

    product_list_view = get_class('dashboard.catalogue.views',
                                  'ProductListView')
    product_lookup_view = get_class('dashboard.catalogue.views',
                                    'ProductLookupView')
    product_create_redirect_view = get_class('dashboard.catalogue.views',
                                             'ProductCreateRedirectView')
    product_createupdate_view = get_class('dashboard.catalogue.views',
                                          'ProductCreateUpdateView')
    product_delete_view = get_class('dashboard.catalogue.views',
                                    'ProductDeleteView')

    product_class_create_view = get_class('dashboard.catalogue.views',
                                          'ProductClassCreateView')
    product_class_update_view = get_class('dashboard.catalogue.views',
                                          'ProductClassUpdateView')
    product_class_list_view = get_class('dashboard.catalogue.views',
                                        'ProductClassListView')
    product_class_delete_view = get_class('dashboard.catalogue.views',
                                          'ProductClassDeleteView')

    category_list_view = get_class('dashboard.catalogue.views',
                                   'CategoryListView')
    category_detail_list_view = get_class('dashboard.catalogue.views',
                                          'CategoryDetailListView')
    category_create_view = get_class('dashboard.catalogue.views',
                                     'CategoryCreateView')
    category_update_view = get_class('dashboard.catalogue.views',
                                     'CategoryUpdateView')
    category_delete_view = get_class('dashboard.catalogue.views',
                                     'CategoryDeleteView')

    stock_alert_view = get_class('dashboard.catalogue.views',
                                 'StockAlertListView')

    def get_urls(self):
        urls = [
            path('products/<int:pk>/', self.product_createupdate_view.as_view(),
                name='catalogue-product'),
            path('products/create/', self.product_create_redirect_view.as_view(),
                name='catalogue-product-create'),
            path('products/create/<slug:product_class_slug>/', self.product_createupdate_view.as_view(),
                name='catalogue-product-create'),
            re_path(r'^products/(?P<parent_pk>[-\d]+)/create-variant/$',
                self.product_createupdate_view.as_view(),
                name='catalogue-product-create-child'),
            path('products/<int:pk>/delete/', self.product_delete_view.as_view(),
                name='catalogue-product-delete'),
            path('', self.product_list_view.as_view(),
                name='catalogue-product-list'),
            path('stock-alerts/', self.stock_alert_view.as_view(),
                name='stock-alert-list'),
            path('product-lookup/', self.product_lookup_view.as_view(),
                name='catalogue-product-lookup'),
            path('categories/', self.category_list_view.as_view(),
                name='catalogue-category-list'),
            path('categories/<int:pk>/', self.category_detail_list_view.as_view(),
                name='catalogue-category-detail-list'),
            path('categories/create/', self.category_create_view.as_view(),
                name='catalogue-category-create'),
            path('categories/create/<int:parent>', self.category_create_view.as_view(),
                name='catalogue-category-create-child'),
            path('categories/<int:pk>/update/', self.category_update_view.as_view(),
                name='catalogue-category-update'),
            path('categories/<int:pk>/delete/', self.category_delete_view.as_view(),
                name='catalogue-category-delete'),
            path('product-type/create/', self.product_class_create_view.as_view(),
                name='catalogue-class-create'),
            path('product-types/', self.product_class_list_view.as_view(),
                name='catalogue-class-list'),
            path('product-type/<int:pk>/update/', self.product_class_update_view.as_view(),
                name='catalogue-class-update'),
            path('product-type/<int:pk>/delete/', self.product_class_delete_view.as_view(),
                name='catalogue-class-delete'),
        ]
        return self.post_process_urls(urls)


application = CatalogueApplication()
