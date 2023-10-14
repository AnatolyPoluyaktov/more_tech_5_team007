import { create } from "zustand";

type BankBranchStore = {
  atms: Array<Atm>;
  branches: Array<BankBranch>;
  clickedBranch: CompleteBankBranch | null;
  setBranches: (branches: BankBranch[]) => void;
  setCompleteBranch: (branch: CompleteBankBranch | null) => void;
};

type BankBranch = {
  id: number;
  latitude: string;
  longitude: string;
  address: string;
  sale_point_name: string;
  office_type: string;
  status: string;
};

type Atm = {
  id: number;
  latitude: string;
  longitude: string;
  all_day: boolean;
  address: string;
};

export type CompleteBankBranch = {
  id: number;
  lat: number;
  lng: number;
  address: string;
  name: string;
};

const useBankBranchesStore = create<BankBranchStore>((set) => ({
  branches: [],
  clickedBranch: null,
  atms: [],
  setBranches: (branches) =>
    set((state) => ({
      ...state,
      branches,
    })),
  setCompleteBranch: (branch) => {
    set((state) => ({
      ...state,
      clickedBranch: branch,
    }));
  },
}));

export default useBankBranchesStore;
