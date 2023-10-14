from src.settings import BASE_DIR
from django.db import migrations, models
from pydantic import BaseModel
from datetime import time
from collections import defaultdict
import datetime
import json
from enum import StrEnum
import random

with (BASE_DIR / "src" / "core" / "migrations" / "init_data" / "002_offices.json").open("r") as f:
    offices = json.load(f)

with (BASE_DIR / "src" / "core" / "migrations" / "init_data" / "002_atms.json").open("r") as f:
    atms = json.load(f)


class DaysOfWeek(StrEnum):
    MONDAY = "MON"
    TUESDAY = "TUE"
    WEDNESDAY = "WED"
    THURSDAY = "THU"
    FRIDAY = "FRI"
    SATURDAY = "SAT"
    SUNDAY = "SUN"


# map_day_of_week: {
#     "пн": DaysOfWeek.MONDAY,
#     "вт": DaysOfWeek.TUESDAY,
#     "cр": DaysOfWeek.WEDNESDAY,
#     "чт": DaysOfWeek.THURSDAY,
#     "пт": DaysOfWeek.FRIDAY,
#     "сб": DaysOfWeek.SATURDAY,
#     "вс": DaysOfWeek.SUNDAY,
# }
# map_num_of_week: {
#     "пн": 1,
#     "вт": 2,
#     "cр": 3,
#     "чт": 4,
#     "пт": 5,
#     "сб": 6,
#     "вс": 7,
# }
# class Schedule(BaseModel):
#     days: str
#     hours: str
#
#     @property
#     def days_of_week(self):
#         day = map_day_of_week.get(self.days)
#         if "Не обслуживает ЮЛ" in day:
#             return None
#         sep = None
#         if "-" in day:
#             sep=","
#         elif "," in day:
#             sep="-"
#         if sep:
#             self.days.split(sep)
#             first_day = day[0]
#             end_day  = day[1]
#             num_first_day = map_num_of_week[first_day]
#             num_end_day = map_num_of_week[end_day]
#             days_of_week = list(map_day_of_week.keys())
#             included_days = []
#             for index, my_day in enumerate(days_of_week, start=1):
#                 if index >= num_first_day and index <=num_end_day:
#                     included_days.append(my_day)
#             return included_days
#         return [day]
#
#     @property
#     def is_served(self):
#         return  False if  "Не обслуживает ЮЛ" in self.days else True
#     def get_time(self):
#         if self.hours is None:
#             return None
#         if "Выходной" in self.hour:
#             return None
#         times = self.hours.split(",")
#         return {
#             "start_time": datetime.datetime.strptime(times[0], "%H:%M").time(),
#             "end_time": datetime.datetime.strptime(times[1], "%H:%M").time()
#         }
#     def is_weekend(self):
#         return False if "Выходной" in self.days else True
#
# def create_schedule_for_legal_entity(data):
#     schedules = []
#     for day in data:
#         schedule = Schedule(**day)
#         schedule.append(schedule)
#      return schedules
#
# def create_model_schedules(model, data):
#
#     for shcedule in models:
#
#
#
#
def fill_offices(Model, SchedulModel):
    for office in offices:
        office_obj = Model(
            sale_point_name=office.get("salePointName"),
            address=office.get("address"),
            status="open",
            rko=random.choice([True, False]),
            office_type=office.get("officeType"),
            sale_point_format=office.get("salePointFormat"),
            suo_avialability=random.choice([True, False]),
            has_ramp=random.choice([True, False]),
            latitude=office.get("latitude"),
            longitude=office.get("longitude"),
            metro_station=office.get("metroStation")
        )
        office_obj.save()
        for day in list(DaysOfWeek):
            legal = SchedulModel(
                office=office_obj,
                days_of_week=day,
                open_time=None if day in [DaysOfWeek.SATURDAY, DaysOfWeek.SUNDAY] else time(hour=10),
                close_time=None if day in [DaysOfWeek.SATURDAY, DaysOfWeek.SUNDAY] else time(hour=20),
                service_mode=1,
                is_serves=True,
                is_weekend=True if day in [DaysOfWeek.SATURDAY, DaysOfWeek.SUNDAY] else False,

            )
            individ = SchedulModel(
                office=office_obj,
                days_of_week=day,
                open_time=None if day in [DaysOfWeek.SATURDAY, DaysOfWeek.SUNDAY] else time(hour=10),
                close_time=None if day in [DaysOfWeek.SATURDAY, DaysOfWeek.SUNDAY] else time(hour=20),
                service_mode=2,
                is_serves=True,
                is_weekend=True if day in [DaysOfWeek.SATURDAY, DaysOfWeek.SUNDAY] else False,

            )
            legal.save()
            individ.save()


def fill_atms(Model, ServiceModel):
    for atm in atms.get("atms"):
        atm_obj = Model(
            address=atm.get("address"),
            latitude=atm.get("latitude"),
            longitude=atm.get("longitude"),
            all_day=atm.get("allDay"),
        )
        atm_obj.save()
        for service in atm.get("services").keys():
            service = ServiceModel(
                atm=atm_obj,
                service=service,
                service_capability=atm.get("services")[service]["serviceCapability"],
                service_activity=atm.get("services")[service]["serviceActivity"],

            )
            service.save()




def forwards_func(apps, schema_editor):
    Office = apps.get_model("core", "Office")
    Schedule = apps.get_model("core", "schedule")
    fill_offices(Office, Schedule)
    Atm = apps.get_model("core", "Atm")
    Atm_services = apps.get_model("core", "AtmService")
    fill_atms(Atm, Atm_services)


def reverse_func(apps, schema_editor):
    Office = apps.get_model("core", "Office")
    Office.objects.all().delete()
    Atm = apps.get_model("core", "Atm")
    Atm.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
