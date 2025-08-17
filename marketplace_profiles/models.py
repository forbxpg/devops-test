"""Модуль моделей акков для ботов."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from constants.enums import ProfileType
from topvector import settings
from topvector.abstracts import AbstractDateTimeModel


class MarketplaceProfile(AbstractDateTimeModel):
    """Модель аккаунта бота."""

    login = models.CharField(
        _("Логин (номер телефона)"),
        max_length=settings.PHONE_NUMBER_MAX_LENGTH,
    )
    phone = models.CharField(
        _("Номер телефона"),
        max_length=settings.PHONE_NUMBER_MAX_LENGTH,
    )
    email = models.EmailField(
        _("Email"),
        unique=True,
        blank=True,
        null=True,
    )
    full_name = models.CharField(
        _("Имя профиля"),
        max_length=settings.PROFILE_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )

    # Credentials
    token = models.TextField(
        _("Токен авторизации"),
        blank=True,
        null=True,
    )
    useragent = models.TextField(
        _("User-Agent"),
        blank=True,
        null=True,
    )
    device_id = models.TextField(
        _("Device ID"),
        blank=True,
        null=True,
    )
    wbaas_token = models.TextField(
        _("WBAAS Token"),
        blank=True,
        null=True,
    )
    cookies = models.TextField(
        _("Cookies"),
        blank=True,
        null=True,
    )
    card_number_part = models.CharField(
        _("Номер карты (часть)"),
        max_length=settings.CARD_NUMBER_MAX_LENGTH,
        blank=True,
        null=True,
    )
    is_token_valid = models.BooleanField(
        _("Валидный токен"),
        default=False,
    )

    # Wildberries
    type = models.CharField(
        _("Тип профиля"),
        choices=ProfileType.choices,
        default=ProfileType.UNSPECIFIED,
        max_length=settings.TEXT_CHOICES_MAX_LENGTH,
    )
    qr_code = models.TextField(
        _("QR Code"),
        blank=True,
        null=True,
    )
    dbs_code = models.CharField(
        _("Код получения"),
        max_length=settings.DBS_CODE_MAX_LENGTH,
        blank=True,
        null=True,
    )

    total_spent = models.PositiveIntegerField(
        _("Суммарно потрачено"),
        default=0,
    )
    postpayment_limit = models.PositiveIntegerField(
        _("Лимит постоплаты"),
        blank=True,
        null=True,
    )
    postpayment_goods_limit = models.PositiveIntegerField(
        _("Лимит постоплаты на товары"),
        blank=True,
        null=True,
    )
    purchase_sum = models.PositiveIntegerField(
        _("Сумма выкупа"),
        blank=True,
        null=True,
    )
    purchase_percent = models.PositiveIntegerField(
        _("Процент выкупа"),
        blank=True,
        null=True,
    )
    proxy = models.ForeignKey(
        "MarketplaceProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="marketplace_profiles",
        db_column="proxy_id",
    )

    class Meta:
        managed = False
        db_table = "marketplace_profiles"

    def __str__(self) -> str:
        return "<MarketplaceProfile %(id)d; %(phone)s; %(full_name)s>" % {
            "id": self.pk,
            "phone": self.phone,
            "full_name": self.full_name,
        }
