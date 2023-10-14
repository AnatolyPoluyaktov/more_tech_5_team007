import { FC } from "react";
import "./FilterButton.css";

interface FilterButtonProps {
  clicked: Boolean;
  onClick: (bol: Boolean) => void;
  label: string;
}

const FilterButton: FC<FilterButtonProps> = ({ clicked, onClick, label }) => {
  let className = "filter-button";
  if (clicked) {
    className += " filter-button_clicked";
  }
  return (
    <button className={className} onClick={() => onClick(!clicked)}>
      {label}
    </button>
  );
};

export default FilterButton;
