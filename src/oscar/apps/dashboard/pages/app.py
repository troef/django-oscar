
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class FlatPageManagementApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    list_view = get_class('dashboard.pages.views', 'PageListView')
    create_view = get_class('dashboard.pages.views', 'PageCreateView')
    update_view = get_class('dashboard.pages.views', 'PageUpdateView')
    delete_view = get_class('dashboard.pages.views', 'PageDeleteView')

    def get_urls(self):
        """
        Get URL patterns defined for flatpage management application.
        """
        urls = [
            path('', self.list_view.as_view(), name='page-list'),
            path('create/', self.create_view.as_view(), name='page-create'),
            path('update/<slug:pk>/', self.update_view.as_view(), name='page-update'),
            path('delete/<int:pk>/', self.delete_view.as_view(), name='page-delete')
        ]
        return self.post_process_urls(urls)


application = FlatPageManagementApplication()
