
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class OffersDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    list_view = get_class('dashboard.offers.views', 'OfferListView')
    metadata_view = get_class('dashboard.offers.views', 'OfferMetaDataView')
    condition_view = get_class('dashboard.offers.views', 'OfferConditionView')
    benefit_view = get_class('dashboard.offers.views', 'OfferBenefitView')
    restrictions_view = get_class('dashboard.offers.views',
                                  'OfferRestrictionsView')
    delete_view = get_class('dashboard.offers.views', 'OfferDeleteView')
    detail_view = get_class('dashboard.offers.views', 'OfferDetailView')

    def get_urls(self):
        urls = [
            path('', self.list_view.as_view(), name='offer-list'),
            # Creation
            path('new/name-and-description/', self.metadata_view.as_view(),
                name='offer-metadata'),
            path('new/condition/', self.condition_view.as_view(),
                name='offer-condition'),
            path('new/incentive/', self.benefit_view.as_view(),
                name='offer-benefit'),
            path('new/restrictions/', self.restrictions_view.as_view(),
                name='offer-restrictions'),
            # Update
            path('<int:pk>/name-and-description/', self.metadata_view.as_view(update=True),
                name='offer-metadata'),
            path('<int:pk>/condition/', self.condition_view.as_view(update=True),
                name='offer-condition'),
            path('<int:pk>/incentive/', self.benefit_view.as_view(update=True),
                name='offer-benefit'),
            path('<int:pk>/restrictions/', self.restrictions_view.as_view(update=True),
                name='offer-restrictions'),
            # Delete
            path('<int:pk>/delete/', self.delete_view.as_view(), name='offer-delete'),
            # Stats
            path('<int:pk>/', self.detail_view.as_view(),
                name='offer-detail'),
        ]
        return self.post_process_urls(urls)


application = OffersDashboardApplication()
