"""Enum для Review."""

from django.db import models
from django.utils.translation import gettext_lazy as _


class ReviewStatus(models.TextChoices):
    """Статус в базе."""

    CREATED = "CREATED", _("Создан")
    QUEUE = "QUEUE", _("В очереди")
    COMPLETED = "COMPLETED", _("Написан")
    NOT_COMPLETED = "NOT_COMPLETED", _("Не написан")


class ReviewInternalStatus(models.TextChoices):
    """Внутренний статус."""

    ACCEPTED = "ACCEPTED", _("Принят")
    EXCLUDED = "EXCLUDED", _("Исключен")
    CHECKING = "CHECKING", _("На проверке")
    UNSPECIFIED = "UNSPECIFIED", _("Не определен")


