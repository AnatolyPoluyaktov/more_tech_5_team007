import pandas as pd
from pandas import
def make_time_series(history_data_path, workload_name="person_per_window") -> pd.DataFrame:
    """
    Make extra dates when office/atms does not work, fill them zero

    workload_name: Name of feature in json file

    history data file example:
    {"data":
        [{"bank_id": 1, "timestamp": "2022-10-14 02:00:00", "person_per_window": 1.0769230769230769, "registered_person_per_service": 2.238095238095238},
        {"bank_id": 2, "timestamp": "2022-10-14 03:00:00", "person_per_window": 3.4, "registered_person_per_service": 2.5714285714285716},
        {"bank_id": 3, "timestamp": "2022-10-14 04:00:00", "person_per_window": 3.3333333333333335, "registered_person_per_service": 2.5},
        ...
        ]
    }
    """
    history_df = pd.read_json(history_data_path)
    df = [pd.Series(history_df.loc[i, :][0]) for i in history_df.index]
    df = pd.DataFrame(df)
    df_original = df[["timestamp", workload_name]].copy()
    df_original = df_original.rename({workload_name: "target"}, axis=1)

    min_date = df_original["timestamp"][0]
    max_date = df_original["timestamp"][df_original.shape[0] - 1]

    date_range = pd.date_range(start=min_date, end=max_date, freq="1H")

    df_original_tr = pd.DataFrame(date_range, columns=["timestamp"])

    df_original = df_original.set_index("timestamp")

    df_original_tr["target"] = 0
    for i, time in enumerate(df_original_tr["timestamp"]):
        if str(time) in df_original.index:
            df_original_tr.loc[i, "target"] = df_original.loc[str(time), "target"]

    df_original_tr = df_original_tr.set_index("timestamp")
    df_original_tr = df_original_tr.asfreq('H')
    return df_original_tr


def get_time_series(df_time_series: pd.DataFrame, model_path: str, horizon: int = 24) -> pd.Series:
    forecaster_loaded = load(model_path)
    forecaster_loaded.fit(df_time_series.iloc[:, 0])
    time_series_pred = forecaster_loaded.predict(steps=horizon)

    time_series_pred = time_series_pred.apply(lambda x: 0 if (x < 0) else x)
    return time_series_pred