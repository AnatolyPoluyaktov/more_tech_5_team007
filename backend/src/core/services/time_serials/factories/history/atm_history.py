from pydantic import BaseModel
from datetime import datetime, timedelta
import random
import json


def calculate_people_per_hour(total_people, num_atms, time_per_person):
    minutes_per_hour = 60

    total_time = total_people * time_per_person
    total_people_per_hour = (total_time / minutes_per_hour) * num_atms

    return total_people_per_hour


class WorkLoadAtmMetrics(BaseModel):
    atm_id: int
    person_per_atm: float
    person_per_hour: float


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

    def person_per_atm(self):
        return random.randint(1, 100) / random.randint(5, 10)

    def person_per_hours(self):
        return calculate_people_per_hour(
            random.randint(1, 100), random.randint(5, 10), random.randint(5, 30)
        )

    def build(self):
        return [
            WorkLoadAtmMetrics(
                atm_id=1,
                timestamp=timestamp,
                person_per_atm=self.person_per_atm(),
                person_per_hour=self.person_per_hours(),
            ).dict()
            for timestamp in self.generate_next_hour()
        ]

    def create_files(self):
        with open("atm_history.json", "w") as f:
            json.dump({"data": self.build()}, f)


if __name__ == "__main__":
    HistorticalFactories().create_files()
