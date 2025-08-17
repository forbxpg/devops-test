"""Модель выкупа в БД."""

from django.db import models
from django.utils.translation import gettext_lazy as _

from constants.enums import (
    PurchaseStatus,
    PurchaseType,
    PurchaseDeliveryType,
    PurchaseMarketplace,
    PurchaseInternalStatus,
)
from topvector.abstracts import AbstractArticleDateTimeModel
from topvector import settings


class Purchase(AbstractArticleDateTimeModel):
    """Модель выкупа в БД."""

    query = models.CharField(
        _("Запрос"),
        max_length=settings.QUERY_MAX_LENGTH,
        blank=True,
        null=True,
    )
    pvz = models.TextField(
        _("Адрес запроса"),
        blank=True,
        null=True,
    )
    status = models.CharField(
        _("Статус в базе"),
        max_length=settings.TEXT_CHOICES_MAX_LENGTH,
        choices=PurchaseStatus.choices,
        default=PurchaseStatus.CREATED,
    )
    marketplace = models.CharField(
        _("Маркетплейс"),
        max_length=settings.TEXT_CHOICES_MAX_LENGTH,
        choices=PurchaseMarketplace.choices,
        default=PurchaseMarketplace.WILDBERRIES,
    )
    type = models.CharField(
        _("Тип оплаты"),
        max_length=settings.TEXT_CHOICES_MAX_LENGTH,
        choices=PurchaseType.choices,
        default=PurchaseType.UNSPECIFIED,
    )
    delivery_type = models.CharField(
        _("Тип доставки"),
        choices=PurchaseDeliveryType.choices,
        default=PurchaseDeliveryType.UNSPECIFIED,
        max_length=settings.TEXT_CHOICES_MAX_LENGTH,
    )

    # Wildberries purchase metadata
    internal_order_id = models.CharField(
        _("Внутренний ID"),
        max_length=settings.ORDER_ID_MAX_LENGTH,
        blank=True,
        null=True,
    )
    name = models.CharField(
        _("Название"),
        max_length=settings.PURCHASE_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    internal_status = models.CharField(
        _("Внутренний статус"),
        max_length=settings.TEXT_CHOICES_MAX_LENGTH,
        choices=PurchaseInternalStatus.choices,
        default=PurchaseInternalStatus.UNSPECIFIED,
    )
    pickup_point_id = models.PositiveBigIntegerField(
        _("ID ПВЗ"),
        blank=True,
        null=True,
    )
    pickup_point_address = models.TextField(
        _("Адрес ПВЗ в Wildberries"),
        blank=True,
        null=True,
    )

    # Money
    amount = models.FloatField(
        _("Стоимость товара"),
        blank=True,
        null=True,
    )
    total_amount = models.FloatField(
        _("Полная стоимость товара"),
        blank=True,
        null=True,
    )
    delivery_amount = models.FloatField(
        _("Стоимость доставки"),
        blank=True,
        null=True,
    )
    pay_state = models.SmallIntegerField(
        _("Pay state"),
        null=True,
        blank=True,
    )
    bitrix_id = models.PositiveIntegerField(
        _("ID Битрикс"),
        blank=True,
        null=True,
    )

    # Seller data
    seller_id = models.PositiveBigIntegerField(
        _("ID селлера"),
        blank=True,
        null=True,
    )
    seller_name = models.CharField(
        _("Имя селлера"),
        max_length=settings.SELLER_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    seller_full_name = models.CharField(
        _("Полное имя селлера"),
        max_length=settings.SELLER_FULL_NAME_MAX_LENGTH,
        blank=True,
        null=True,
    )
    seller_inn = models.CharField(
        _("ИНН селлера"),
        max_length=settings.SELLER_INN_MAX_LENGTH,
        blank=True,
        null=True,
    )

    # Dates
    bought_at = models.DateTimeField(
        _("Дата выкупа"),
        null=True,
        blank=True,
    )
    arrived_at = models.DateTimeField(
        _("Дата прихода"),
        null=True,
        blank=True,
    )
    expired_at = models.DateTimeField(
        _("Дата окончания срока хранения"),
        null=True,
        blank=True,
    )
    last_refund_date = models.DateTimeField(
        _("Последняя дата возврата"),
        null=True,
        blank=True,
    )
    last_date = models.DateTimeField(
        _("Последняя дата"),
        null=True,
        blank=True,
    )
    claim_expire_date = models.DateTimeField(
        _("Дата окончания срока получения"),
        null=True,
        blank=True,
    )

    profile = models.ForeignKey(
        "marketplace_profiles.MarketplaceProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="purchases",
        verbose_name=_("Профиль выкупа"),
        db_index=True,
        db_column="profile_id",
    )

    class Meta:
        managed = False
        db_table = "purchases"

    def __str__(self) -> str:
        return "<Purchase %(id)d, %(article)s, %(status)s, %(address)s>" % {
            "id": self.pk,
            "article": self.article,
            "status": self.status,
            "address": self.pickup_point_address,
        }
