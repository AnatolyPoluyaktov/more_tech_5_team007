import { useEffect } from "react";
import { Filters, YandexMap, useBankBranchesStore } from "../../../widgets";
import "./SearchBankBranch.css";
import logo from "./imgs/logo_light.png";

const SearchBankBranch = () => {
  const bankBranchesStore = useBankBranchesStore();
  useEffect(() => {
    fetch("http://146.190.161.174:8000/api/offices/")
      .then((response) => response.json())
      .then((json) => bankBranchesStore.setBranches(json))
      .catch((e) => console.log(e));
  }, []);
  const rootClassName = "search-bank-branch";
  return (
    <>
      <header className={`${rootClassName}__header`}>
        <img className={`${rootClassName}__logo`} src={logo} />
      </header>
      <main className={`${rootClassName}__main`}>
        <YandexMap />
        <Filters />
      </main>
    </>
  );
};

export default SearchBankBranch;
