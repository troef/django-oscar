
from oscar.core.application import DashboardApplication
from oscar.core.loading import get_class
from django.urls import path


class PartnersDashboardApplication(DashboardApplication):
    name = None
    default_permissions = ['is_staff', ]

    list_view = get_class('dashboard.partners.views', 'PartnerListView')
    create_view = get_class('dashboard.partners.views', 'PartnerCreateView')
    manage_view = get_class('dashboard.partners.views', 'PartnerManageView')
    delete_view = get_class('dashboard.partners.views', 'PartnerDeleteView')

    user_link_view = get_class('dashboard.partners.views',
                               'PartnerUserLinkView')
    user_unlink_view = get_class('dashboard.partners.views',
                                 'PartnerUserUnlinkView')
    user_create_view = get_class('dashboard.partners.views',
                                 'PartnerUserCreateView')
    user_select_view = get_class('dashboard.partners.views',
                                 'PartnerUserSelectView')
    user_update_view = get_class('dashboard.partners.views',
                                 'PartnerUserUpdateView')

    def get_urls(self):
        urls = [
            path('', self.list_view.as_view(), name='partner-list'),
            path('create/', self.create_view.as_view(),
                name='partner-create'),
            path('<int:pk>/', self.manage_view.as_view(),
                name='partner-manage'),
            path('<int:pk>/delete/', self.delete_view.as_view(),
                name='partner-delete'),

            path('<int:partner_pk>/users/add/', self.user_create_view.as_view(),
                name='partner-user-create'),
            path('<int:partner_pk>/users/select/', self.user_select_view.as_view(),
                name='partner-user-select'),
            path('<int:partner_pk>/users/<int:user_pk>/link/', self.user_link_view.as_view(), name='partner-user-link'),
            path('<int:partner_pk>/users/<int:user_pk>/unlink/', self.user_unlink_view.as_view(), name='partner-user-unlink'),
            path('<int:partner_pk>/users/<int:user_pk>/update/', self.user_update_view.as_view(),
                name='partner-user-update'),
        ]
        return self.post_process_urls(urls)


application = PartnersDashboardApplication()
