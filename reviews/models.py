"""Модуль для моделей отзывов."""

from typing import TYPE_CHECKING

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from topvector.abstracts import AbstractArticleDateTimeModel
from topvector import settings


class Review(AbstractArticleDateTimeModel):
    """Модель отзыва в БД."""

    pros = models.TextField(
        _("Достоинства"),
        blank=True,
        null=True,
    )
    cons = models.TextField(
        _("Недостатки"),
        blank=True,
        null=True,
    )
    comment = models.TextField(
        _("Отзыв"),
        blank=True,
        null=True,
    )
    rating = models.PositiveSmallIntegerField(
        _("Рейтинг отзыва"),
        validators=[
            MaxValueValidator(settings.REVIEW_MAX_RATING),
            MinValueValidator(settings.REVIEW_MIN_RATING),
        ],
    )
    image_url = models.TextField(
        _("URLы фоток к отзыву"),
        blank=True,
        null=True,
    )
    video_url = models.TextField(
        _("URLы видео к отзыву"),
        blank=True,
        null=True,
    )
    profile = models.ForeignKey(
        "marketplace_profiles.MarketplaceProfile",
        on_delete=models.SET_NULL,
        related_name="reviews",
        blank=True,
        null=True,
        db_column="profile_id",
        verbose_name=_("Аккаунт"),
    )

    class Meta:
        managed = False
        db_table = "reviews"

    def __str__(self):
        return "<Review %(id)d; %(article)s, %(comment)s %(profile_id)s>" % {
            "id": self.pk,
            "article": self.article,
            "comment": self.comment,
            "profile_id": self.pr,
        }
