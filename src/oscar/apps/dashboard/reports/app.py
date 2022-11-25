
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class ReportsApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    index_view = get_class('dashboard.reports.views', 'IndexView')

    def get_urls(self):
        urls = [
            path('', self.index_view.as_view(), name='reports-index'),
        ]
        return self.post_process_urls(urls)


application = ReportsApplication()
