from __future__ import unicode_literals

from django.db import models

from django.db.models import (
    CharField,
    IntegerField,
    TextField)

from activflow.core.models import AbstractActivity, AbstractInitialActivity

class CaseFoo(AbstractInitialActivity):
    """Sample representation of Foo activity"""
    bar = CharField("Bar", max_length=200, validators=[])
    baz = CharField(verbose_name="Baz", max_length=30, choices=(
        ('CR', 'Corge'), ('WL', 'Waldo')))
    qux = TextField("Qux", blank=True)

    def clean(self):
        """Custom validation logic should go here"""
        pass


class CaseCorge(AbstractActivity):
    """Sample representation of Corge activity"""
    grault = CharField("Grault", max_length=50)
    thud = IntegerField("Thud")

    def clean(self):
        """Custom validation logic should go here"""
        pass