import datetime
import pandas as pd


def range_alg_offices(data: dict) -> list[int]:
    """
    return ranged list of bank_id

    data example
    {"data":
        [{"bank_id": 1, "distance_auto": 333, "distance_foot": 9097, "distance_moto": 238, "time_auto": "1:06:54", "time_foot": "3:22:13", "time_moto": "3:23:36", "person_per_window": 5.1875, "registered_person_per_service": 4.631578947368421},
        {"bank_id": 2, "distance_auto": 7772, "distance_foot": 4580, "distance_moto": 7660, "time_auto": "4:57:36", "time_foot": "3:44:56", "time_moto": "2:03:11", "person_per_window": 13.571428571428571, "registered_person_per_service": 2.0},
        {"bank_id": 3, "distance_auto": 2096, "distance_foot": 2492, "distance_moto": 4139, "time_auto": "3:38:28", "time_foot": "3:00:42", "time_moto": "3:49:35", "person_per_window": 4.764705882352941, "registered_person_per_service": 1.3076923076923077},
        {"bank_id": 4, "distance_auto": 3853, "distance_foot": 5838, "distance_moto": 4979, "time_auto": "0:48:52", "time_foot": "0:39:10", "time_moto": "4:00:47", "person_per_window": 3.1052631578947367, "registered_person_per_service": 3.2857142857142856},
        {"bank_id": 5, "distance_auto": 151, "distance_foot": 6188, "distance_moto": 6063, "time_auto": "2:24:30", "time_foot": "3:40:58", "time_moto": "2:32:10", "person_per_window": 1.4210526315789473, "registered_person_per_service": 15.2}]
    }
    """

    def get_time_in_minuets(time_str: str):
        time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S").time()
        total_seconds = datetime.timedelta(
            hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second
        ).total_seconds()
        return total_seconds / 60

    df_load = pd.from_dict(data)
    data_list = [pd.Series(x) for x in df_load]
    df = pd.DataFrame(data_list)
    df = df.set_index("bank_id")
    df[["time_auto", "time_foot", "time_moto"]] = df[
        ["time_auto", "time_foot", "time_moto"]
    ].applymap(get_time_in_minuets)

    df["mean_time"] = df[["time_auto", "time_foot", "time_moto"]].mean(axis=1)

    range_list = df["person_per_window"] * df["mean_time"]

    range_list.sort_values(inplace=True)

    return list(range_list.index)
