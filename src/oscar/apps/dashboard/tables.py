from django_tables2 import Table
from django.utils.translation import ngettext_lazy


class DashboardTable(Table):
    caption = ngettext_lazy('%d Row', '%d Rows')

    def get_caption_display(self):
        # Allow overriding the caption with an arbitrary string that we cannot
        # interpolate the number of rows in
        try:
            return self.caption % self.paginator.count
        except TypeError:
            pass
        return self.caption

    class Meta:
        template = 'dashboard/table.html'
        attrs = {'class': 'table table-striped table-bordered'}
