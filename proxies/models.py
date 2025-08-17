"""Модуль для моделей прокси."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from topvector import settings
from topvector.abstracts import AbstractDateTimeModel


class Proxy(AbstractDateTimeModel):
    """Модель прокси в бд."""

    is_active = models.BooleanField(
        _("Активный"),
        default=True,
    )
    is_busy = models.BooleanField(
        _("Занят"),
        default=False,
    )
    name = models.CharField(
        _('Сервер ("username:password@ip:port")'),
        max_length=settings.PROXY_NAME_MAX_LENGTH,
    )

    class Meta:
        managed = False
        db_table = "proxies"
