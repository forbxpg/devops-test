"""Модуль для абстрактных моделей."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from topvector import settings


class AbstractDateTimeModel(models.Model):
    """Абстрактная модель created_at/updated_at."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("-created_at",)


class AbstractArticleDateTimeModel(AbstractDateTimeModel):
    """Абстрактная модель с created_at/updated_at и article."""

    article = models.CharField(
        _("Артикул выкупа"),
        max_length=settings.ARTICLE_MAX_LENGTH,
    )

    class Meta:
        abstract = True
