from django.db import models
from django.utils.translation import gettext_lazy as _


class PurchaseStatus(models.TextChoices):
    """Статусы в панели."""

    CREATED = "CREATED", _("Создан")
    QUEUE = "QUEUE", _("В очереди")
    DELIVERY = "DELIVERY", _("В доставке")
    PICKUP_POINT = "PICKUP_POINT", _("На ПВЗ")
    COMPLETED = "COMPLETED", _("Завершен")
    NOT_COMPLETED = "NOT_COMPLETED", _("Не выполнен")


class PurchaseType(models.TextChoices):
    """Тип оплаты."""

    PREPAYMENT = "PREPAYMENT", _("Предоплата")
    POSTPAYMENT = "POSTPAYMENT", _("Постоплата")
    UNSPECIFIED = "UNSPECIFIED", _("Не указано")


class PurchaseInternalStatus(models.TextChoices):
    """Внутренний статус выкупа."""

    PURCHASED = "PURCHASED", _("Оплачен")
    REFUND = "REFUND", _("Возврат")
    REJECTED = "REJECTED", _("Отказ")
    FAILED_PAYMENT = "FAILED_PAYMENT", _("Ошибка оплаты")
    UNSPECIFIED = "UNSPECIFIED", _("Не указано")


class PurchaseMarketplace(models.TextChoices):
    """Маркетплейс выкупа."""

    OZON = "OZON", _("OZON")
    WILDBERRIES = "WILDBERRIES", _("WILDBERRIES")
    UNSPECIFIED = "UNSPECIFIED", _("Не указано")


class PurchaseDeliveryType(models.TextChoices):
    """Тип доставки."""

    SELF = "SELF", _("В пункт выдачи")
    COURIER = "COURIER", _("Курьером")
    UNSPECIFIED = "UNSPECIFIED", _("Не указано")
