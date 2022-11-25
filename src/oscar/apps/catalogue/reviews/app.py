from django.contrib.auth.decorators import login_required

from oscar.core.application import Application
from oscar.core.loading import get_class
from django.urls import path


class ProductReviewsApplication(Application):
    name = None
    hidable_feature_name = "reviews"

    detail_view = get_class('catalogue.reviews.views', 'ProductReviewDetail')
    create_view = get_class('catalogue.reviews.views', 'CreateProductReview')
    vote_view = get_class('catalogue.reviews.views', 'AddVoteView')
    list_view = get_class('catalogue.reviews.views', 'ProductReviewList')

    def get_urls(self):
        urls = [
            path('<int:pk>/', self.detail_view.as_view(),
                name='reviews-detail'),
            path('add/', self.create_view.as_view(),
                name='reviews-add'),
            path('<int:pk>/vote/', login_required(self.vote_view.as_view()),
                name='reviews-vote'),
            path('', self.list_view.as_view(), name='reviews-list'),
        ]
        return self.post_process_urls(urls)


application = ProductReviewsApplication()
