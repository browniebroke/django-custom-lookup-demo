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

    def __init__(self, lhs, rhs):
        # Save actual right hand side value
        self._real_rhs = rhs
        super().__init__(lhs, rhs)

    @property
    def rhs(self):
        # Replace rhs attribute with current time as the ORM 
        # doesn't like a boolean value passed to a date lookup
        return timezone.now()

    @rhs.setter
    def rhs(self, value):
        # just a fake setter
        pass

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        direction = '<' if self._real_rhs is True else '>='
        print(lhs, rhs, params)
        return f'%s {direction} %s' % (lhs, rhs), params


Post._meta.get_field('published_at').register_lookup(BooleanPastDate)
