from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    def is_published(self) -> bool:
        return (self.published_at is not None
                and self.published_at < timezone.now())


# New in Django 4.2: custom lookup
from django.db.models import Lookup


class BooleanPastDate(Lookup):
    lookup_name = 'past'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        direction = '<' if rhs is True else '>='
        print(lhs, rhs, params)
        return f'%s {direction} %s' % (lhs, timezone.now().isoformat()), params


Post._meta.get_field('published_at').register_lookup(BooleanPastDate)
