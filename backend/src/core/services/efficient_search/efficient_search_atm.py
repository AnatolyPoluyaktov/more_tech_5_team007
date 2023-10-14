import datetime
import pandas as pd


def range_alg_atms(data_path) -> list[int]:
    """
    return ranged list of atm_id

    data example
    {"data":
        [{"atm_id": 1, "distance_auto": 5360, "distance_foot": 4863, "distance_moto": 772, "time_auto": "4:35:46", "time_foot": "1:23:41", "time_moto": "2:40:09", "person_per_atm": 7.714285714285714, "person_per_hour": 304.5},
        {"atm_id": 2, "distance_auto": 1366, "distance_foot": 8604, "distance_moto": 2756, "time_auto": "2:05:02", "time_foot": "4:14:04", "time_moto": "2:18:18", "person_per_atm": 1.0, "person_per_hour": 48.6},
        {"atm_id": 3, "distance_auto": 999, "distance_foot": 228, "distance_moto": 6939, "time_auto": "2:36:46", "time_foot": "4:43:12", "time_moto": "2:41:44", "person_per_atm": 13.857142857142858, "person_per_hour": 140.83333333333334},
        {"atm_id": 4, "distance_auto": 1462, "distance_foot": 2770, "distance_moto": 2385, "time_auto": "0:42:04", "time_foot": "3:06:04", "time_moto": "1:21:51", "person_per_atm": 2.9, "person_per_hour": 46.66666666666667},
        {"atm_id": 5, "distance_auto": 9196, "distance_foot": 8539, "distance_moto": 2334, "time_auto": "1:52:53", "time_foot": "2:22:23", "time_moto": "1:10:07", "person_per_atm": 4.0, "person_per_hour": 14.933333333333334}]
    }
    """

    def get_time_in_minuets(time_str: str):
        time_obj = datetime.datetime.strptime(time_str, "%H:%M:%S").time()
        total_seconds = datetime.timedelta(
            hours=time_obj.hour, minutes=time_obj.minute, seconds=time_obj.second
        ).total_seconds()
        return total_seconds / 60

    df_load = pd.read_json(data_path)
    data_list = [pd.Series(x) for x in df_load["data"]]
    df = pd.DataFrame(data_list)
    df = df.set_index("atm_id")

    df[["time_auto", "time_foot", "time_moto"]] = df[
        ["time_auto", "time_foot", "time_moto"]
    ].applymap(get_time_in_minuets)

    df["mean_time"] = df[["time_auto", "time_foot", "time_moto"]].mean(axis=1)

    range_list = df["person_per_atm"] * df["mean_time"]

    range_list.sort_values(inplace=True)

    return list(range_list.index)


range_alg_atms("atms_example.json")
