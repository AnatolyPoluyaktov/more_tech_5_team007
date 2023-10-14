import { create } from "zustand";

interface FiltersStore {
  atms: Boolean;
  offices: Boolean;
  person: Boolean;
  company: Boolean;
  withoutWeekends: Boolean;
  mortgage: Boolean;
  peopleWithDisabilities: Boolean;
  bioData: Boolean;
  installApp: Boolean;
  lessWorkload: Boolean;
  setFilter: (key: keyof FiltersStore, clicked: Boolean) => void;
}

const useFiltersStore = create<FiltersStore>((set) => ({
  atms: false,
  offices: true,
  person: true,
  company: false,
  withoutWeekends: false,
  mortgage: false,
  peopleWithDisabilities: false,
  bioData: false,
  installApp: false,
  lessWorkload: false,
  setFilter: (key: keyof FiltersStore, clicked: Boolean) =>
    set((state) => ({
      ...state,
      [key]: clicked,
    })),
}));

export default useFiltersStore;
