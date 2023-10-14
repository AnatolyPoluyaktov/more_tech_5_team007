from django.db import models


class DaysOfWeek(models.TextChoices):
    MONDAY = "MON", "Пн"
    TUESDAY = "TUE", "Вт"
    WEDNESDAY = "WED", "Ср"
    THURSDAY = "THU", "Чт"
    FRIDAY = "FRI", "Пт"
    SATURDAY = "SAT", "Сб"
    SUNDAY = "SUN", "Вс"
