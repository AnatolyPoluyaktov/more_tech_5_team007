import { useState } from "react";
import "./BranchInput.css";

const BranchInput = () => {
  const [value, setValue] = useState("");
  const [isFocused, setIsFocused] = useState(false);
  const searchIcon = isFocused ? "" : "branch-input_search";
  return (
    <input
      onFocus={() => {
        setIsFocused(true);
      }}
      onBlur={() => {
        setIsFocused(false);
      }}
      className={searchIcon + " branch-input"}
      placeholder="Введите адрес"
      value={value}
      onChange={(e) => {
        setValue(e.target.value);
      }}
    />
  );
};

export default BranchInput;
