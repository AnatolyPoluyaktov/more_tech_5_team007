import os

from celery import Celery
from src.core.services.time_serials.time_series import make_time_series, get_time_series
from celery.schedules import crontab
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "str.settings")

app = Celery("core")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


def predict_office_workload():
    from src.core.services.time_serials.factories.history.office_history import (
        HistorticalFactories,
    )

    data = HistorticalFactories().build()
    history_time_series = make_time_series({"data": data})
    get_time_series(
        history_time_series,
        model_path="src/core/services/time_serials/forecaster_xgb.py",
    )


def predict_atm_workload():
    from src.core.services.time_serials.factories.history.atm_history import (
        HistorticalFactories,
    )

    data = HistorticalFactories().build()
    history_time_seriaes = make_time_series({"data": data}, "person_per_atm")
    return get_time_series(
        history_time_seriaes,
        model_path="src/core/services/time_serials/forecaster_xgb.py",
    )


@app.task(name="core.perform_predict_for_every_office")
def perform_predict_for_every_office():
    from src.core.models import Office
    offices = []
    for office in Office.objects.all():
        workload = predict_office_workload()
        office.workloads=workload
        office.append(office)

    Office.objects.bulk_update(offices,fields=["workloads"])

@app.task(name="core.perform_predict_for_every_atm")
def perform_predict_for_every_atm():
    from src.core.models import Atm
    offices = []
    for atm in Atm.objects.all():
        workload = predict_atm_workload()
        atm.workloads = workload
        atm.append(atm)

    Atm.objects.bulk_update(offices, fields=["workloads"])

    @app.on_after_finalize.connect
    def setup_periodic_tasks(sender, **kwargs):


        sender.add_periodic_task(
            crontab(hour=0, minute=0, day_of_week="*"),
            predict_office_workload.s(),
            name="predict_office_workload",
        )
        sender.add_periodic_task(
            crontab(hour=0, minute=0, day_of_week="*"),
            predict_atm_workload.s(),
            name="predict_atm_workload",
        )

