
from oscar.apps.promotions.models import KeywordPromotion, PagePromotion
from oscar.core.application import Application
from oscar.core.loading import get_class
from django.urls import path


class PromotionsApplication(Application):
    name = 'promotions'

    home_view = get_class('promotions.views', 'HomeView')
    record_click_view = get_class('promotions.views', 'RecordClickView')

    def get_urls(self):
        urls = [
            path('page-redirect/<int:page_promotion_id>/', self.record_click_view.as_view(model=PagePromotion),
                name='page-click'),
            path('keyword-redirect/<int:keyword_promotion_id>/', self.record_click_view.as_view(model=KeywordPromotion),
                name='keyword-click'),
            path('', self.home_view.as_view(), name='home'),
        ]
        return self.post_process_urls(urls)


application = PromotionsApplication()
