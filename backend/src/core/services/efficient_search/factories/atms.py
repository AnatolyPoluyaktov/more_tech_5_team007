import json

from pydantic import BaseModel
from datetime import timedelta
import random


class WorkLoadAtmMetrics(BaseModel):
    atm_id: int
    distance_auto: int
    distance_foot: int
    distance_moto: int
    time_auto: str
    time_foot: str
    time_moto: str
    person_per_atm: float
    person_per_hour: float


class WorkloadOAtmsMetricsFactories:
    def __init__(self):
        self.seq: int = 0
        self.gen_id = self._generate_next_id()

    def _generate_next_id(self):
        while True:
            self.seq += 1
            yield self.seq

    def generate_distance(self):
        return {
            "distance_auto": random.randint(100, 10000),
            "distance_foot": random.randint(100, 10000),
            "distance_moto": random.randint(100, 10000),
        }

    def time_distance(self):
        return {
            "time_auto": str(timedelta(seconds=random.randint(1000, 18000))),
            "time_foot": str(timedelta(seconds=random.randint(1000, 18000))),
            "time_moto": str(timedelta(seconds=random.randint(1000, 18000))),
        }

    def person_per_atm(self):
        return random.randint(1, 100) / random.randint(5, 10)

    def person_per_hours(self):
        return calculate_people_per_hour(
            random.randint(1, 100), random.randint(5, 10), random.randint(5, 30)
        )

    def build(self, size):
        return [
            WorkLoadAtmMetrics(
                atm_id=next(self.gen_id),
                **self.generate_distance(),
                **self.time_distance(),
                person_per_atm=self.person_per_atm(),
                person_per_hour=self.person_per_hours()
            ).dict()
            for _ in range(size)
        ]

    def create_files(self, size):
        with open("atms.json", "w") as f:
            json.dump({"data": self.build(size)}, f)
