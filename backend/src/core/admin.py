from django.contrib import admin
from src.core.models import (
    Atm,
    AtmService,
    Office,
    Schedule,
)

admin.site.register(Atm)
admin.site.register(AtmService)
admin.site.register(Office)
admin.site.register(Schedule)
