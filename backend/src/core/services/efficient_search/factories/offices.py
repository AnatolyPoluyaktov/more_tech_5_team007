import json

from pydantic import BaseModel
from datetime import timedelta
import random

NUM_BANKS = 200
NUM_ATM = 800


class WorkloadOfficMetrics(BaseModel):
    bank_id: int
    distance_auto: int
    distance_foot: int
    distance_moto: int
    time_auto: str
    time_foot: str
    time_moto: str
    person_per_window: float
    registered_person_per_service: float


class WorkloadOfficesMetricsFactories:
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

    def person_per_window(self):
        return random.randint(1, 100) / random.randint(5, 32)

    def registered_person_per_service(self):
        return random.randint(1, 100) / random.randint(5, 35)

    def build(self, size):
        return [
            WorkloadOfficMetrics(
                bank_id=next(self.gen_id),
                **self.generate_distance(),
                **self.time_distance(),
                person_per_window=self.person_per_window(),
                registered_person_per_service=self.registered_person_per_service()
            ).dict()
            for _ in range(size)
        ]

    def create_files(self, size):
        with open("offices.json", "w") as f:
            json.dump({"data": self.build(size)}, f)
