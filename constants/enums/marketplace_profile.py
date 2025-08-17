"""Модуль для енумов Акков"""

from django.db import models
from django.utils.translation import gettext_lazy as _


class ProfileType(models.TextChoices):
    """Тип профиля."""

    WILDBERRIES = "WILDBERRIES", _("WILDBERRIES")
    WILDBERRIES_BOT = "WILDBERRIES_BOT", _("WILDBERRIES_BOT")
    OZON = "OZON", _("OZON")
    UNSPECIFIED = "UNSPECIFIED", _("Не указано")
