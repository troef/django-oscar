
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class ReviewsApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    list_view = get_class('dashboard.reviews.views', 'ReviewListView')
    update_view = get_class('dashboard.reviews.views', 'ReviewUpdateView')
    delete_view = get_class('dashboard.reviews.views', 'ReviewDeleteView')

    def get_urls(self):
        urls = [
            path('', self.list_view.as_view(), name='reviews-list'),
            path('<int:pk>/', self.update_view.as_view(),
                name='reviews-update'),
            path('<int:pk>/delete/', self.delete_view.as_view(),
                name='reviews-delete'),
        ]
        return self.post_process_urls(urls)


application = ReviewsApplication()
