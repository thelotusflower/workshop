from django.db.models import QuerySet


class BlogSectionQS(QuerySet):
    def all_section_with_auto_at_start(self):
        return self.filter(name__startswith='Авто')