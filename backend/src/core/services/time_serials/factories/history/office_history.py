from pydantic import BaseModel
from datetime import datetime, timedelta
import random
import json


class WorkloadOfficMetrics(BaseModel):
    bank_id: int
    timestamp: str
    person_per_window: float
    registered_person_per_service: float


class HistorticalFactories:
    def __init__(self):
        self.seq: int = 0
        self.gen_id = self._generate_next_id()

    def _generate_next_id(self):
        while True:
            self.seq += 1
            yield self.seq

    def generate_next_hour(self):
        current_date = datetime.now()
        year_ago = current_date - timedelta(days=365)

        hour = timedelta(hours=1)
        current_hour = datetime(
            year_ago.year, year_ago.month, year_ago.day, year_ago.hour
        )

        while current_hour <= current_date:
            if current_hour.hour == 20:
                current_hour += timedelta(days=1)
                current_hour = current_hour.replace(hour=9)
            yield current_hour.strftime("%Y-%m-%d %H:%M:%S")
            current_hour += hour

    def person_per_window(self):
        return random.randint(1, 100) / random.randint(5, 32)

    def registered_person_per_service(self):
        return random.randint(1, 100) / random.randint(5, 35)

    def build(self):
        return [
            WorkloadOfficMetrics(
                bank_id=1,
                timestamp=timestamp,
                person_per_window=self.person_per_window(),
                registered_person_per_service=self.registered_person_per_service(),
            ).dict()
            for timestamp in self.generate_next_hour()
        ]

    def create_files(self):
        with open("offices_history.json", "w") as f:
            json.dump({"data": self.build()}, f)


if __name__ == "__main__":
    HistorticalFactories().create_files()
